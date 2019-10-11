from rolepy.generate.biomes import Biome
from rolepy.generate.names import ForestNameGenerator
from rolepy.generate.names import MountainNameGenerator


class Zone:

    def __init__(self, biome):
        self.biome = biome
        self.frontier = list()
        self.inside = list()
        self.name = ""
        if self.biome == Biome.MOUNTAIN:
            self.name = MountainNameGenerator.get()
        elif self.biome == Biome.FOREST:
            self.name = ForestNameGenerator.get()
        self.size = 0

    def __repr__(self):
        return "Zone<{biome} ({size}): \"{name}\">".format(
            biome=self.biome.name,
            size=self.size,
            name=self.name
        )

    def add(self, position):
        self.inside.append(position)
        self.size += 1

    def barycenter(self):
        def mean(l):
            return sum(l) / len(l)
        return (
            mean([p[0] for p in self.inside]),
            mean([p[1] for p in self.inside])
        )
