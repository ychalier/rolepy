from rolepy.generate.biomes import classify_biome


class BiomeMap(dict):
    """Infinite array of biome types per position."""

    def __init__(self, temperature_heatmap, humidity_heatmap):
        super(BiomeMap, self).__init__(self)
        self.temperature_heatmap = temperature_heatmap
        self.humidity_heatmap = humidity_heatmap

    def build(self, positions):
        """Classify a set of positions into biomes, and store the result."""
        for i, j in positions:
            self[i, j] = classify_biome(
                self.temperature_heatmap[i, j],
                self.humidity_heatmap[i, j]
            )
