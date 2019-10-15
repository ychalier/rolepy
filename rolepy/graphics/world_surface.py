import logging
import pygame
from rolepy.globals import SPRITE_SIZE
from rolepy.misc import Position


class WorldSurface:

    def __init__(self, tile_manager, world):
        self.tile_manager = tile_manager
        self.world = world
        self.surface = pygame.Surface((0, 0), pygame.SRCALPHA | pygame.HWSURFACE, 32)
        self.offset_x = 0
        self.offset_y = 0
        self.is_checking = False

    def build(self, targets=list()):
        logging.debug("Building world surface")
        positions = self.world.terrain.keys()
        min_x = min([p.x for p in positions])
        max_x = max([p.x for p in positions])
        min_y = min([p.y for p in positions])
        max_y = max([p.y for p in positions])
        new_surface = pygame.Surface(
            (
                (max_x - min_x + 1) * SPRITE_SIZE,
                (max_y - min_y + 1) * SPRITE_SIZE
            ),
            pygame.SRCALPHA, 32)
        new_surface.blit(self.surface, (
            (- self.offset_x - min_x) * SPRITE_SIZE,
            (- self.offset_y - min_y) * SPRITE_SIZE
        ))
        if len(targets) > 0:
            for position in targets:
                for tile in self.world.terrain[position]:
                    new_surface.blit(self.tile_manager.terrain[tile].sprite(), (
                        (position.x - min_x) * SPRITE_SIZE,
                        (position.y - min_y) * SPRITE_SIZE,
                    ))
        else:
            for position, layers in self.world.terrain.items():
                for tile in layers:
                    new_surface.blit(self.tile_manager.terrain[tile].sprite(), (
                        (position.x - min_x) * SPRITE_SIZE,
                        (position.y - min_y) * SPRITE_SIZE,
                    ))
        self.offset_x = - min_x
        self.offset_y = - min_y
        self.surface = new_surface

    def check(self, camera):
        if self.is_checking:
            return
        self.is_checking = True
        keys = frozenset(self.world.terrain.keys())
        margin = 30
        need_to_generate = False

        for x in range(int(camera.x) - margin, int(camera.x) + margin + 1):
            for y in range(int(camera.y) - margin, int(camera.y) + margin + 1):
                if Position(x, y) not in keys:
                    need_to_generate = True
                    break
            if need_to_generate:
                break
        if need_to_generate:
            margin = int(margin * 1.5)
            logging.debug("Generating new terrain")
            targets = list()
            for x in range(int(camera.x) - margin, int(camera.x) + margin + 1):
                for y in range(int(camera.y) - margin, int(camera.y) + margin + 1):
                    if Position(x, y) not in keys:
                        self.world.generate(x, y)
                        targets.append(Position(x, y))
            self.build(targets=targets)
        self.is_checking = False
