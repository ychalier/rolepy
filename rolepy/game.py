import logging
import pygame
import pygame.locals
import time
import sys
from rolepy.misc import Position
from rolepy.model import World
from rolepy.globals import Direction
from rolepy.graphics import Render
from rolepy.graphics import MoveCamera
from rolepy.graphics import TileManager


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

    def load(self):
        logging.info("Loading game")
        t_start = time.time()
        logging.debug("Loading sprites")
        self.tile_manager.load()
        logging.debug("Loading world")
        self.world.load()
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
                        if not self.camera_is_moving:
                            player_tile.direction = Direction.NORTH
                            MoveCamera(self, self.camera
                                       + Position(0, 1), 32, .2).start()
                    elif event.key == pygame.locals.K_DOWN:
                        if not self.camera_is_moving:
                            player_tile.direction = Direction.SOUTH
                            MoveCamera(self, self.camera
                                       + Position(0, -1), 32, .2).start()
                    elif event.key == pygame.locals.K_LEFT:
                        if not self.camera_is_moving:
                            player_tile.direction = Direction.WEST
                            MoveCamera(self, self.camera
                                       + Position(-1, 0), 32, .2).start()
                    elif event.key == pygame.locals.K_RIGHT:
                        if not self.camera_is_moving:
                            player_tile.direction = Direction.EAST
                            MoveCamera(self, self.camera
                                       + Position(1, 0), 32, .2).start()
            if time.time() - last_frame > 1 / self.settings.max_fps:
                rendering = Render(self)
                rendering.start()
                rendering.join()
                last_frame = time.time()
