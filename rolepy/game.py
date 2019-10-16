import logging
import pygame
import pygame.locals
import time
import sys
from rolepy.misc import Position
from rolepy.misc import Fifo
from rolepy.model import World
from rolepy.model import DetectZone
from rolepy.globals import Ordinal
from rolepy.graphics import Render
from rolepy.graphics import MoveCamera
from rolepy.graphics import TileManager
from rolepy.graphics import WorldSurface
from rolepy.graphics import Interface
from rolepy.graphics import InterfaceBox


class Game:

    def __init__(self, settings):
        self.settings = settings
        self.screen = None
        self.clock = None
        self.renderer = None
        self.tile_manager = TileManager()
        self.world = World()
        self.camera = Position(0, 0)
        self.camera_is_moving = False
        self.world_surface = WorldSurface(self.tile_manager, self.world)
        self.interface = Interface(self.settings.resolution)
        self.fps_interface_box = InterfaceBox(self.interface, 77, 29)
        self.zone_interface_box = InterfaceBox(self.interface, 151, 29)
        self.is_moving = False
        self.is_detecting_zone = False
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
        logging.debug("Loading fonts")
        self.interface.load()
        self.interface.boxes[Position(8, 8)] = self.fps_interface_box
        self.interface.boxes[Position(8, self.settings.resolution[1] - 37)] = self.zone_interface_box
        logging.debug("Loading world")
        self.world.load()
        self.world_surface.build()
        logging.info("Done loading, took {elapsed} seconds".format(
            elapsed=time.time() - t_start))

    def start(self):
        logging.debug("Creating window of size "
                      + str(self.settings.resolution))
        self.screen = pygame.display.set_mode(
            self.settings.resolution, pygame.DOUBLEBUF | pygame.HWSURFACE)
        pygame.key.set_repeat(self.settings.key_repeat_delay)
        self.clock = pygame.time.Clock()
        last_frame = time.time()
        logging.debug("Entering main loop")
        player_tile = self.tile_manager.entities[self.world.player]
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
                        MoveCamera(self, Ordinal.NORTH).start()
                    elif event.key == pygame.locals.K_DOWN:
                        MoveCamera(self, Ordinal.SOUTH).start()
                    elif event.key == pygame.locals.K_LEFT:
                        MoveCamera(self, Ordinal.WEST).start()
                    elif event.key == pygame.locals.K_RIGHT:
                        MoveCamera(self, Ordinal.EAST).start()
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
            now = time.time()
            if self.settings.max_fps is None or now - last_frame > 1 / self.settings.max_fps:
                if now == last_frame:
                    fps.add(1e3)
                else:
                    fps.add(1 / (now - last_frame))
                self.fps_interface_box.update("fps: {}".format(round(fps.mean)))
                if not self.is_detecting_zone:
                    DetectZone(self, *self.camera.pair()).start()
                rendering = Render(self)
                rendering.start()
                rendering.join()
                last_frame = now
