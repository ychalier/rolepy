import pygame
from rolepy.globals import SPRITE_SIZE
from rolepy.misc import Position


class WorldSurface(pygame.Surface):
    """Represent one fixed-size piece of world surface."""

    SIZE = 121

    def __init__(self, tile_manager, world, center):
        pygame.Surface.__init__(
            self,
            (WorldSurface.SIZE * SPRITE_SIZE, WorldSurface.SIZE * SPRITE_SIZE),
            pygame.SRCALPHA | pygame.HWSURFACE,
            32
        )
        self.tile_manager = tile_manager
        self.world = world
        self.center = center
        self.offset = Position(
            WorldSurface.SIZE // 2 - round(center.x),
            WorldSurface.SIZE // 2 - round(center.y)
        )

    def build(self):
        """Blits the terrain tiles onto the surface."""
        target = self.center.target()
        range_x = range(target.x - WorldSurface.SIZE // 2, target.x + WorldSurface.SIZE // 2 + 1)
        range_y = range(target.y - WorldSurface.SIZE // 2, target.y + WorldSurface.SIZE // 2 + 1)
        for j, pos_x in enumerate(range_x):
            for i, pos_y in enumerate(range_y):
                layers = self.world.terrain.get(Position(pos_x, pos_y), None)
                if layers is None:
                    self.world.generate(pos_x, pos_y)
                    layers = self.world.terrain[Position(pos_x, pos_y)]
                for tile in layers:
                    self.blit(self.tile_manager.terrain[tile].sprite(), (
                        j * SPRITE_SIZE,
                        i * SPRITE_SIZE,
                    ))
