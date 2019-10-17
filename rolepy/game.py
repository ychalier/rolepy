import logging
import pygame
import pygame.locals
import time
import sys
from rolepy.misc import Position
from rolepy.misc import Fifo
from rolepy.model import World
from rolepy.tasks import DetectZone
from rolepy.tasks import MoveCamera
from rolepy.tasks import TaskManager
from rolepy.globals import Ordinal
from rolepy.graphics import Render
from rolepy.graphics.assets import TileManager
from rolepy.graphics.terrain import WorldSurfaceManager
from rolepy.graphics.interface import InterfaceManager


class Game:

    def __init__(self, settings):
        self.settings = settings
        self.screen = None
        self.tile_manager = TileManager()
        self.world = World()
        self.camera = Position(0, 0)
        self.world_surface_manager = WorldSurfaceManager(self.tile_manager, self.world, Position(0, 0))
        self.interface_manager = InterfaceManager(self.settings.resolution)
        self.task_manager = TaskManager()
        self.movements = {
            Ordinal.EAST: False,
            Ordinal.NORTH: False,
            Ordinal.WEST: False,
            Ordinal.SOUTH: False
        }
        self.speed = 5

    def load(self):
        logging.info("Loading game")
        t_start = time.time()
        logging.debug("Loading sprites")
        self.tile_manager.load()
        logging.debug("Loading interfaces")
        self.interface_manager.load()
        logging.debug("Loading world")
        self.world.load()
        self.world_surface_manager.load()
        logging.info("Done loading, took {elapsed} seconds".format(
            elapsed=time.time() - t_start))

    def start(self):
        logging.debug("Creating window of size "
                      + str(self.settings.resolution))
        self.screen = pygame.display.set_mode(
            self.settings.resolution, pygame.DOUBLEBUF | pygame.HWSURFACE)
        pygame.display.set_caption("RolePy")
        pygame.display.set_icon(pygame.image.load("assets/logo.png"))
        pygame.key.set_repeat(self.settings.key_repeat_delay)
        last_frame = time.time()
        logging.debug("Entering main loop")
        player_tile = self.tile_manager.entities[self.world.player.texture]
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
                        self.task_manager.start(MoveCamera(self, Ordinal.NORTH))
                    elif event.key == pygame.locals.K_DOWN:
                        self.task_manager.start(MoveCamera(self, Ordinal.SOUTH))
                    elif event.key == pygame.locals.K_LEFT:
                        self.task_manager.start(MoveCamera(self, Ordinal.WEST))
                    elif event.key == pygame.locals.K_RIGHT:
                        self.task_manager.start(MoveCamera(self, Ordinal.EAST))
                    elif event.key == pygame.locals.K_LSHIFT:
                        self.speed = 10
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.locals.K_UP:
                        self.movements[Ordinal.NORTH] = False
                    elif event.key == pygame.locals.K_DOWN:
                        self.movements[Ordinal.SOUTH] = False
                    elif event.key == pygame.locals.K_LEFT:
                        self.movements[Ordinal.WEST] = False
                    elif event.key == pygame.locals.K_RIGHT:
                        self.movements[Ordinal.EAST] = False
                    elif event.key == pygame.locals.K_LSHIFT:
                        self.speed = 5
                    elif event.key == pygame.locals.K_F1:
                        self.interface_manager.increment_state()
            now = time.time()
            self.world_surface_manager.update(self.camera, self.task_manager)
            if self.settings.max_fps is None or now - last_frame > 1 / self.settings.max_fps:
                if now == last_frame:
                    fps.add(1e3)
                else:
                    fps.add(1 / (now - last_frame))
                self.interface_manager[InterfaceManager.DEBUG_INTERFACE].fps.update("fps: {}".format(round(fps.mean)))
                self.interface_manager[InterfaceManager.DEBUG_INTERFACE].pos.update("x: {}, y: {}".format(*self.camera.target().pair()))
                zone = self.world.get_zone(*self.camera.pair())
                if zone is None:
                    self.task_manager.start(DetectZone(self, *self.camera.pair()))
                else:
                    self.interface_manager[InterfaceManager.DEBUG_INTERFACE].zone.update(zone.name)
                rendering = Render(self)
                rendering.start()
                rendering.join()
                last_frame = now
