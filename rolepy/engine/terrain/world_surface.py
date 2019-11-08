import time
import logging
import pygame
from rolepy.engine.core.globals import SPRITE_SIZE
from rolepy.engine.core.structs import Position


class WorldSurface(pygame.Surface):
    """Represent one fixed-size piece of world surface."""

    SIZE = 131

    def __init__(self, tile_manager, world, center):
        pygame.Surface.__init__(
            self,
            (WorldSurface.SIZE * SPRITE_SIZE, WorldSurface.SIZE * SPRITE_SIZE),
            pygame.HWSURFACE | pygame.DOUBLEBUF,
            32
        )
        self.tile_manager = tile_manager
        self.world = world
        self.center = center
        self.offset = Position(
            WorldSurface.SIZE // 2 - round(center.x),
            WorldSurface.SIZE // 2 - round(center.y)
        )

    def build(self, delay=None, range_offset=None):
        """Blits the terrain tiles onto the surface."""
        t_start = time.time()
        target = self.center.target()
        range_x = [target.x - WorldSurface.SIZE // 2, target.x + WorldSurface.SIZE // 2 + 1]
        range_y = [target.y - WorldSurface.SIZE // 2, target.y + WorldSurface.SIZE // 2 + 1]
        offset_j = 0
        offset_i = 0
        if range_offset is not None:
            if range_offset.x > 0:
                range_x[1] -= WorldSurface.SIZE // 2
            elif range_offset.x < 0:
                range_x[0] += WorldSurface.SIZE // 2
                offset_j = WorldSurface.SIZE // 2
            elif range_offset.y > 0:
                range_y[1] -= WorldSurface.SIZE // 2
            elif range_offset.y < 0:
                range_y[0] += WorldSurface.SIZE // 2
                offset_i += WorldSurface.SIZE // 2
        for j, pos_x in enumerate(range(*range_x)):
            if delay is not None:
                time.sleep(delay)
            for i, pos_y in enumerate(range(*range_y)):
                layers = self.world.terrain.get(Position(pos_x, pos_y), None)
                if layers is None:
                    self.world.generate(pos_x, pos_y)
                    layers = self.world.terrain[Position(pos_x, pos_y)]
                for tile in layers:
                    self.blit(self.tile_manager.terrain[tile].sprite(), (
                        (offset_j + j) * SPRITE_SIZE,
                        (offset_i + i) * SPRITE_SIZE,
                    ))
        logging.debug("Built surface at %s in %ss", self.center, round(time.time() - t_start, 4))

    def build_from(self, surface, offset, delay=None):
        self.blit(surface, (SPRITE_SIZE * offset).pair())
        self.build(delay=delay, range_offset=offset)
