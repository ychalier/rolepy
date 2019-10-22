from rolepy.generate.biomes import Biome
from rolepy.generate.names import get_forest_name
from rolepy.generate.names import get_mountain_name


class Zone:
    """Represent a symbolic connex set of biome-constant positions."""

    def __init__(self, biome):
        self.biome = biome
        self.frontier = list()
        self.inside = list()
        self.name = ""
        self.size = 0

    def __repr__(self):
        return "Zone<{biome} ({size}): \"{name}\">".format(
            biome=self.biome.name,
            size=self.size,
            name=self.name
        )

    def find_name(self):
        """Provides a name for the zone, based on its type and position."""
        i, j = self.barycenter()
        seed = str(i) + str(j)
        if self.biome == Biome.MOUNTAIN:
            self.name = get_mountain_name(seed)
        elif self.biome == Biome.FOREST:
            self.name = get_forest_name(seed)

    def add(self, position):
        """Append a position to the zone."""
        self.inside.append(position)
        self.size += 1

    def barycenter(self):
        """Compute the barycenter of the known positions in the zone."""
        def mean(arr):
            return sum(arr) / len(arr)
        return (
            mean([p[0] for p in self.inside]),
            mean([p[1] for p in self.inside])
        )
