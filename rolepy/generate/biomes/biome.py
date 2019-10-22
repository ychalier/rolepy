import enum


@enum.unique
class Biome(enum.Enum):
    """Represent a biome type."""
    EMPTY = 0
    PLAIN = 1
    FOREST = 2
    MOUNTAIN = 3
    DESERT = 4


def classify_biome(temperature, humidity):
    """Return the biome type given climatic features."""
    if temperature < -.5 and humidity < 0:
        return Biome.MOUNTAIN
    if temperature > .5 and humidity < -.5:
        return Biome.DESERT
    if humidity > .1:
        return Biome.FOREST
    return Biome.PLAIN
