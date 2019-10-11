from rolepy.generate.biomes import Biome
from rolepy.generate.biomes import Zone


class BiomeMap(dict):

    def __init__(self, temperature_heatmap, humidity_heatmap):
        super(BiomeMap, self).__init__(self)
        self.temperature_heatmap = temperature_heatmap
        self.humidity_heatmap = humidity_heatmap

    def build(self, positions):
        for i, j in positions:
            self[i, j] = Biome.classify(
                self.temperature_heatmap[i, j],
                self.humidity_heatmap[i, j]
            )

    def get_neighbors(self, position):
        i, j = position
        return set([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)])

    def get_zones(self):
        remaining = set(self.keys())
        zones = list()
        while len(remaining) > 0:
            current = remaining.pop()
            zone = Zone(self[current])
            buffer = set()
            buffer.add(current)
            while len(buffer) > 0:
                p = buffer.pop()
                zone.add(p)
                for neighbor in self.get_neighbors(p).intersection(remaining):
                    remaining.remove(neighbor)
                    if self[neighbor] == zone.biome:
                        buffer.add(neighbor)
                    else:
                        zone.frontier.append(neighbor)
            zones.append(zone)
        return zones

    def to_array(self):
        ordinates = [key[0] for key in self.keys()]
        abscissa = [key[1] for key in self.keys()]
        offset_i = min(ordinates)
        offset_j = min(abscissa)
        array = list()
        for i in range(max(ordinates) - offset_i + 1):
            array.append(list())
            for j in range(max(abscissa) - offset_j + 1):
                array[-1].append(Biome.EMPTY.value)
        for (i, j) in self:
            array[i - offset_i][j - offset_j] = self[i, j].value
        return array

    def demo():
        import matplotlib.pyplot as plt
        import matplotlib.colors as cols
        from rolepy.generate import Heatmap
        BIOME_CMAP = cols.ListedColormap(
            ["black", "lightgreen", "forestgreen", "slategrey", "khaki"])
        world = BiomeMap(Heatmap(4379), Heatmap(2933))
        world.build([(i, j) for i in range(-300, 300) for j in range(-300, 300)])
        zones = world.get_zones()
        plt.figure(figsize=(20, 20))
        plt.imshow(world.to_array(), cmap=BIOME_CMAP, vmin=0, vmax=5)
        offset_i = min([key[0] for key in world.keys()])
        offset_j = min([key[1] for key in world.keys()])
        for zone in zones:
            if zone.size < 1000:
                continue
            i, j = zone.barycenter()
            plt.text(j-offset_j, i-offset_i, str(zone), horizontalalignment="center")
        plt.show()
