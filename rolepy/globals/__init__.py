import enum

SPRITE_SIZE = 32  # px


@enum.unique
class TextureTerrain(enum.Enum):
    EMPTY = 0
    GRASS = 1
    PAVED_ROAD = 2


@enum.unique
class TextureEntities(enum.Enum):
    MAN = 0


@enum.unique
class Ordinal(enum.Enum):
    EAST = 0
    NORTH = 1
    WEST = 2
    SOUTH = 3


@enum.unique
class WalkAnimation(enum.Enum):
    LEFT = 0
    REST = 1
    RIGHT = 2
