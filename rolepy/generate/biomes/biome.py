import enum


@enum.unique
class Biome(enum.Enum):
    EMPTY = 0
    PLAIN = 1
    FOREST = 2
    MOUNTAIN = 3
    DESERT = 4

    def classify(temperature, humidity):
        if temperature < -.5 and humidity < 0:
            return Biome.MOUNTAIN
        elif temperature > .5 and humidity < -.5:
            return Biome.DESERT
        elif humidity > .1:
            return Biome.FOREST
        return Biome.PLAIN
