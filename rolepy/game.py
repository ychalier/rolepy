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
from rolepy.globals import TextureEntities
from rolepy.globals import SPRITE_SIZE
from rolepy.graphics.entities import EntityAiThread
from rolepy.graphics.entities import NpcAi
from rolepy.graphics.entities import EntityManager
from rolepy.graphics.entities import Entity


def smooth_translation(source, destination):
    gap = destination - source
    if gap.norm_inf() < .1 / SPRITE_SIZE:
        return destination
    return .01 * (99. * source + destination)

class Game:

    def __init__(self, settings):
        self.settings = settings
        self.screen = None
        self.tile_manager = TileManager()
        self.world = World()
        self.camera = Position(0, 0)
        self.world_surface_manager = WorldSurfaceManager(self.tile_manager, self.world, Position(0, 0))
        self.interface_manager = InterfaceManager(self.settings.resolution)
        self.entity_manager = EntityManager(*map(lambda x: x // SPRITE_SIZE + 1, self.settings.resolution))
        self.task_manager = TaskManager()
        self.movements = {
            Ordinal.EAST: False,
            Ordinal.NORTH: False,
            Ordinal.WEST: False,
            Ordinal.SOUTH: False
        }
        self.player_entity = None
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
        logging.debug("Loading entities")
        self.player_entity = Entity(self.entity_manager, 1, self.tile_manager.entities[TextureEntities.MAN], Position(0, 0), speed=5)
        self.entity_manager.add(self.player_entity)
        self.entity_manager.add(Entity(self.entity_manager, 2, self.tile_manager.entities[TextureEntities.WOMAN], Position(0, 1), ai=NpcAi(Position(0, 1))))
        self.entity_manager.add(Entity(self.entity_manager, 3, self.tile_manager.entities[TextureEntities.WOMAN], Position(0, 2), ai=NpcAi(Position(10, 2))))
        self.entity_manager.update_registry(self.camera)
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
                        # self.task_manager.start(MoveCamera(self, Ordinal.NORTH))
                        self.task_manager.start(self.player_entity.move(Ordinal.NORTH, 1))
                    elif event.key == pygame.locals.K_DOWN:
                        # self.task_manager.start(MoveCamera(self, Ordinal.SOUTH))
                        self.task_manager.start(self.player_entity.move(Ordinal.SOUTH, 1))
                    elif event.key == pygame.locals.K_LEFT:
                        # self.task_manager.start(MoveCamera(self, Ordinal.WEST))
                        self.task_manager.start(self.player_entity.move(Ordinal.WEST, 1))
                    elif event.key == pygame.locals.K_RIGHT:
                        # self.task_manager.start(MoveCamera(self, Ordinal.EAST))
                        self.task_manager.start(self.player_entity.move(Ordinal.EAST, 1))
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
            self.task_manager.start(EntityAiThread(self.entity_manager), log=False)
            self.entity_manager.center = self.camera.target()
            self.camera = smooth_translation(self.camera, self.player_entity.position)
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
