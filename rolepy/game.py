import logging
import time
import sys
import pygame
import pygame.locals
from rolepy.misc import Position
from rolepy.misc import Fifo
from rolepy.model import World
from rolepy.tasks import DetectZone
from rolepy.tasks import TaskManager
from rolepy.globals import Ordinal
from rolepy.graphics import Render
from rolepy.graphics.assets import TileManager
from rolepy.graphics.terrain import WorldSurfaceManager
from rolepy.graphics.interface import InterfaceManager
from rolepy.globals import TextureEntities
from rolepy.globals import SPRITE_SIZE
from rolepy.graphics.entities import EntityAiThread
from rolepy.graphics.entities import NpcAi
from rolepy.graphics.entities import EntityManager
from rolepy.graphics.entities import Entity


def smooth_translation(source, destination):
    """Shifts a source position towards a destination with an ease-in effect."""
    gap = destination - source
    if gap.norm_inf() < .1 / SPRITE_SIZE:
        return destination
    return .01 * (99. * source + destination)

class Game:
    """Main game controller, hosting main routine."""

    def __init__(self, settings):
        self.settings = settings
        self.screen = None
        self.tile_manager = TileManager()
        self.world = World()
        self.camera = Position(0, 0)
        self.world_surface_manager = WorldSurfaceManager(
            self.tile_manager,
            self.world,
            Position(0, 0)
        )
        self.interface_manager = InterfaceManager(self.settings.resolution)
        self.entity_manager = EntityManager(*map(
            lambda x: x // SPRITE_SIZE + 1,
            self.settings.resolution
        ))
        self.task_manager = TaskManager()
        self.player_entity = None

    def load(self):
        """Loads components of the game into the RAM."""
        logging.info("Loading game")
        t_start = time.time()
        logging.debug("Loading sprites")
        self.tile_manager.load()
        logging.debug("Loading interfaces")
        self.interface_manager.load()
        logging.debug("Loading world")
        self.world_surface_manager.load()
        logging.debug("Loading entities")
        self.player_entity = Entity(
            self.entity_manager,
            1,
            self.tile_manager.entities[TextureEntities.MAN],
            position=Position(0, 0),
            speed=5
        )
        self.entity_manager.add(self.player_entity)
        self.entity_manager.add(Entity(
            self.entity_manager,
            2,
            self.tile_manager.entities[TextureEntities.WOMAN],
            position=Position(0, 1),
            brain=NpcAi(Position(0, 1))
        ))
        self.entity_manager.add(Entity(
            self.entity_manager,
            3,
            self.tile_manager.entities[TextureEntities.WOMAN],
            position=Position(0, 2),
            brain=NpcAi(Position(10, 2))
        ))
        self.entity_manager.center = self.camera.target()
        self.entity_manager.update_registry()
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
        self.main()

    def main(self):
        """Main routine of the game."""
        logging.debug("Entering main loop")
        last_frame = time.time()
        fps = Fifo(10)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logging.info("Exiting from QUIT event")
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.locals.K_ESCAPE:
                        logging.info("Exiting from ESC key pressed")
                        sys.exit()
                    elif event.key == pygame.locals.K_UP:
                        self.task_manager.start(
                            self.player_entity.move(Ordinal.NORTH, 1),
                            log=False
                        )
                    elif event.key == pygame.locals.K_DOWN:
                        self.task_manager.start(
                            self.player_entity.move(Ordinal.SOUTH, 1),
                            log=False
                        )
                    elif event.key == pygame.locals.K_LEFT:
                        self.task_manager.start(
                            self.player_entity.move(Ordinal.WEST, 1),
                            log=False
                        )
                    elif event.key == pygame.locals.K_RIGHT:
                        self.task_manager.start(
                            self.player_entity.move(Ordinal.EAST, 1),
                            log=False
                        )
                    elif event.key == pygame.locals.K_LSHIFT:
                        self.player_entity.speed = 10
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.locals.K_LSHIFT:
                        self.player_entity.speed = 5
                    elif event.key == pygame.locals.K_F1:
                        self.interface_manager.increment_state()
            now = time.time()
            self.world_surface_manager.update(self.camera, self.task_manager)
            self.task_manager.start(EntityAiThread(self.entity_manager), log=False)
            self.entity_manager.center = self.camera.target()
            self.camera = smooth_translation(self.camera, self.player_entity.position)
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
