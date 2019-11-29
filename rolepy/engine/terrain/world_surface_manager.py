import logging
from rolepy.engine.core.enums import Ordinal
from rolepy.engine.core.structs import Position
from rolepy.engine.core.misc import angle_direction
from rolepy.engine.terrain import WorldSurface
from rolepy.engine.terrain import SwitchWorldSurface


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

    def load_unit(self, i, j):
        """Build of world surface of the grid."""
        self.surfaces[i][j].build()
        self.surfaces_storage[self.surfaces[i][j].center] = self.surfaces[i][j]

    def load(self, loading_screen):
        """Initial build of the grid of surfaces."""
        loading_screen.next_step("Loading world", 9)
        for pos_i in range(3):
            for pos_j in range(3):
                loading_screen.next_sub_step("Loading WorldSurface #(%d, %d)" % (pos_i, pos_j))
                self.load_unit(pos_i, pos_j)
                loading_screen.done_sub_step()
        loading_screen.done_step()

    def check_surfaces_storage(self):
        """Delete useless surfaces to make rooms for new ones."""
        for surface_center in list(self.surfaces_storage.keys()):
            if (self.center - surface_center).norm() > WorldSurface.SIZE * 10:
                del self.surfaces_storage[surface_center]

    def get_world_surface(self, center, build_delay=.001):
        """Return the world surface at a given position, builds it if necessary."""
        if center in self.surfaces_storage:
            return self.surfaces_storage[center]
        logging.debug("Building surface at (%d, %d)", *center.pair())
        world_surface = WorldSurface(self.tile_manager, self.world, center)
        built = False
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_center = center + Position(
                x * (WorldSurface.SIZE // 2),
                y * (WorldSurface.SIZE // 2)
            )
            if neighbor_center in self.surfaces_storage:
                neighbor_surface = self.surfaces_storage[neighbor_center]
                world_surface.build_from(
                    neighbor_surface,
                    offset=neighbor_center - center,
                    delay=build_delay
                )
                built = True
                break
        if not built:
            world_surface.build(delay=build_delay)
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
        distance = gap.norm()
        if distance > WorldSurface.SIZE // 4 + 1:
            direction = angle_direction(gap.angle())
            task_manager.start(SwitchWorldSurface(self, direction))
