import logging
import time
import math
from rolepy.globals import Ordinal
from rolepy.misc import Position
from rolepy.graphics.terrain import WorldSurface
from rolepy.tasks import SwitchWorldSurface


class WorldSurfaceManager:
    """Manages the surface containing world terrain, aiming to make it
       seem infinite and without loading screens.
       Works by maintaining a 3*3 grid of surroundings surfaces and switching
       between them.
    """

    def __init__(self, tile_manager, world, center):
        self.tile_manager = tile_manager
        self.world = world
        self.surfaces_storage = dict()
        print(center)
        self.surfaces = [
            [
                WorldSurface(
                    self.tile_manager,
                    self.world,
                    center + Position(
                        (j - 1) * (WorldSurface.SIZE // 2),
                        (i - 1) * (WorldSurface.SIZE // 2),
                    )
                )
                for j in range(3)
            ]
            for i in range(3)
        ]
        self.center = center

    def surface(self):
        """Return the center surface."""
        return self.surfaces[1][1]

    def load(self, i=None, j=None):
        """Initial build of the grid of surfaces."""
        if i is None or j is None:
            for pos_i in range(3):
                for pos_j in range(3):
                    self.load(pos_i, pos_j)
            return
        self.surfaces[i][j].build()
        self.surfaces_storage[self.surfaces[i][j].center] = self.surfaces[i][j]

    def check_surfaces_storage(self):
        """Delete useless surfaces to make rooms for new ones."""
        for surface_center in list(self.surfaces_storage.keys()):
            if (self.center - surface_center).norm_inf() > WorldSurface.SIZE * 10:
                del self.surfaces_storage[surface_center]

    def get_world_surface(self, center):
        """Return the world surface at a given position, builds it if necessary."""
        if center in self.surfaces_storage:
            return self.surfaces_storage[center]
        logging.debug("Building surface at (%d, %d)", *center.pair())
        world_surface = WorldSurface(self.tile_manager, self.world, center)
        world_surface.build(delay=.001)
        self.surfaces_storage[center] = world_surface
        self.check_surfaces_storage()
        return world_surface

    def switch(self, direction):
        """Switch from one surface to another."""
        logging.debug("Going %s", direction)
        if direction == Ordinal.EAST:
            new_center = self.surfaces[1][2].center
            for i in range(3):
                self.surfaces[i].pop(0)
            self.center = Position(*new_center.pair())
            time.sleep(.01)
            for i in range(3):
                self.surfaces[i].append(self.get_world_surface(
                    new_center + Position(
                        WorldSurface.SIZE // 2,
                        (i - 1) * (WorldSurface.SIZE // 2)
                    )
                ))
        elif direction == Ordinal.NORTH:
            new_center = self.surfaces[0][1].center
            self.surfaces.pop(2)
            self.center = Position(*new_center.pair())
            time.sleep(.01)
            self.surfaces.insert(0, list())
            for j in range(3):
                self.surfaces[0].append(self.get_world_surface(
                    new_center + Position(
                        (j - 1) * (WorldSurface.SIZE // 2),
                        -(WorldSurface.SIZE // 2)
                    )
                ))
        elif direction == Ordinal.WEST:
            new_center = self.surfaces[1][0].center
            for i in range(3):
                self.surfaces[i].pop(2)
            self.center = Position(*new_center.pair())
            time.sleep(.01)
            for i in range(3):
                self.surfaces[i].insert(0, self.get_world_surface(
                    new_center + Position(
                        -(WorldSurface.SIZE // 2),
                        (i - 1) * (WorldSurface.SIZE // 2)
                    )
                ))
        elif direction == Ordinal.SOUTH:
            new_center = self.surfaces[2][1].center
            self.surfaces.pop(0)
            self.center = Position(*new_center.pair())
            time.sleep(.01)
            self.surfaces.append(list())
            for j in range(3):
                self.surfaces[2].append(self.get_world_surface(
                    new_center + Position(
                        (j - 1) * (WorldSurface.SIZE // 2),
                        WorldSurface.SIZE // 2
                    )
                ))
        logging.debug("Done switching surface.")


    def update(self, position, task_manager):
        """Check if a surface switch is necessary."""
        gap = position - self.center
        distance = gap.norm_inf()
        if distance > WorldSurface.SIZE // 4 + 1:
            angle = gap.angle()
            if math.pi / 4 >= angle > -math.pi / 4:
                task_manager.start(SwitchWorldSurface(self, Ordinal.EAST))
            elif 3 * math.pi / 4 >= angle > math.pi / 4:
                task_manager.start(SwitchWorldSurface(self, Ordinal.SOUTH))
            elif -math.pi / 4 >= angle > -3 * math.pi / 4:
                task_manager.start(SwitchWorldSurface(self, Ordinal.NORTH))
            else:
                task_manager.start(SwitchWorldSurface(self, Ordinal.WEST))
