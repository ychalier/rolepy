import pygame
from rolepy.globals import SPRITE_SIZE


class WorldSurface:

    def __init__(self):
        self.surface = pygame.Surface((0, 0), pygame.SRCALPHA, 32)
        self.offset_x = 0
        self.offset_y = 0

    def build(self, tile_manager, world):
        positions = world.terrain.keys()
        min_x = min([p.x for p in positions])
        max_x = max([p.x for p in positions])
        min_y = min([p.y for p in positions])
        max_y = max([p.y for p in positions])
        del self.surface
        self.surface = pygame.Surface(
            (
                (max_x - min_x + 1) * SPRITE_SIZE,
                (max_y - min_y + 1) * SPRITE_SIZE
            ),
            pygame.SRCALPHA, 32)
        self.offset_x = - min_x
        self.offset_y = - min_y
        for position, layers in world.terrain.items():
            for tile in layers:
                self.surface.blit(tile_manager.terrain[tile].sprite(), (
                    (position.y + self.offset_y) * SPRITE_SIZE,
                    (position.x + self.offset_x) * SPRITE_SIZE,
                ))
