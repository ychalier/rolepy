import pygame
from rolepy.globals import SPRITE_SIZE
from rolepy.misc import Position


class WorldSurface(pygame.Surface):

    SIZE = 141

    def __init__(self, tile_manager, world, center):
        pygame.Surface.__init__(self,
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
        target = self.center.target()
        for j, x in enumerate(range(target.x - WorldSurface.SIZE // 2, target.x + WorldSurface.SIZE // 2 + 1)):
            for i, y in enumerate(range(target.y - WorldSurface.SIZE // 2, target.y + WorldSurface.SIZE // 2 + 1)):
                layers = self.world.terrain.get(Position(x, y), None)
                if layers is None:
                    self.world.generate(x, y)
                    layers = self.world.terrain[Position(x, y)]
                for tile in layers:
                    self.blit(self.tile_manager.terrain[tile].sprite(), (
                        j * SPRITE_SIZE,
                        i * SPRITE_SIZE,
                    ))
