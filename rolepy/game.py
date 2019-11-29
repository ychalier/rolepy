import logging
import time
import pygame
import pygame.locals
from rolepy.engine.core.structs import Fifo
from rolepy.engine.core.tasks import TaskManager
from rolepy.engine.resources import TileManager
from rolepy.engine.graphics import Render
from rolepy.engine.graphics import Camera
from rolepy.engine.terrain import WorldSurfaceManager
from rolepy.engine.interface import InterfaceManager
from rolepy.engine.entities import EntityThread
from rolepy.engine.entities import EntityManager
from rolepy.engine.events import EventManager
from rolepy.engine.inputs import InputManager
from rolepy.model import World
from rolepy.model import Population
from rolepy.generate import DetectZone
from rolepy import LoadingScreen


class Game:
    """Main game controller, hosting main routine."""

    def __init__(self, settings):
        self.settings = settings
        self.screen = None
        self.running = True
        self.population = None
        self.world = World()
        self.camera = Camera()
        self.tile_manager = TileManager()
        self.task_manager = TaskManager()
        self.event_manager = EventManager()
        self.input_manager = InputManager(self)
        self.interface_manager = InterfaceManager(self)
        self.entity_manager = EntityManager(self)
        self.world_surface_manager = WorldSurfaceManager(
            self.tile_manager,
            self.world,
            self.camera.copy()
        )

    def load(self):
        """Loads components of the game into the RAM."""
        logging.info("Loading game")
        t_start = time.time()
        loading_screen = LoadingScreen(self.screen, 3)
        loading_screen.start()
        logging.debug("Loading sprites")
        self.tile_manager.load(loading_screen)
        logging.debug("Loading interfaces")
        self.interface_manager.load()
        logging.debug("Loading world")
        self.world_surface_manager.load(loading_screen)
        logging.debug("Loading entities")
        self.population = Population(self.entity_manager)
        self.entity_manager.load(self.camera, self.population, self.event_manager, loading_screen)
        loading_screen.join()
        logging.info("Done loading, took %f seconds", time.time() - t_start)

    def start(self):
        """Once loaded, setup the window and start the main routine."""
        logging.debug("Creating window of size %d*%d", *self.settings.resolution)
        self.screen = pygame.display.set_mode(
            self.settings.resolution,
            pygame.DOUBLEBUF | pygame.HWSURFACE
        )
        pygame.display.set_caption("RolePy")
        pygame.display.set_icon(pygame.image.load("assets/logo.png"))
        pygame.key.set_repeat(self.settings.key_repeat_delay)

    def quit(self):
        """Quit the game."""
        logging.info("Exiting from QUIT event")
        self.running = False

    def main(self):
        """Main routine of the game."""
        logging.debug("Entering main loop")
        last_frame = time.time()
        fps = Fifo(10)
        while self.running:
            self.input_manager.update()
            now = time.time()
            self.world_surface_manager.update(self.camera, self.task_manager)
            self.task_manager.start(EntityThread(self.entity_manager), log=False)
            self.entity_manager.center = self.camera.target()
            self.camera.smooth_translation(self.entity_manager.player.attributes.position)
            if self.settings.max_fps is None or now - last_frame > 1 / self.settings.max_fps:
                fps.add(1 / max(now - last_frame, .001))
                dbg_if = self.interface_manager[InterfaceManager.DEBUG_INTERFACE]
                dbg_if.fps.update("fps: {}".format(round(fps.mean)))
                dbg_if.pos.update("x: {}, y: {}".format(*self.camera.target().pair()))
                zone = self.world.get_zone(*self.camera.pair())
                if zone is None:
                    self.task_manager.start(DetectZone(self, *self.camera.pair()))
                else:
                    dbg_if.zone.update(zone.name)
                rendering = Render(self)
                rendering.start()
                rendering.join()
                last_frame = now
