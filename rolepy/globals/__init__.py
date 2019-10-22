import enum

SPRITE_SIZE = 16  # px


@enum.unique
class TextureTerrain(enum.Enum):
    """Enumeration of all possible terrain textures."""
    EMPTY = 0
    GRASS_0 = 1
    GRASS_1 = 2
    GRASS_2 = 3
    GRASS_3 = 4
    GRASS_4 = 5
    GRASS_5 = 6
    GRASS_6 = 7
    GRASS_MOUNTAIN = 8
    HOUSE_1 = 9
    HOUSE_2 = 10
    HOUSE_3 = 11
    HOUSE_4 = 12
    HOUSE_5 = 13
    HOUSE_6 = 14
    SAND_0 = 15
    SAND_1 = 16
    SAND_2 = 17
    SAND_3 = 18
    SAND_4 = 19
    SAND_5 = 20
    TREE_LARGE = 21
    TREE_SMALL = 22


@enum.unique
class TextureEntities(enum.Enum):
    """Enumeration of all possible entity textures."""
    MAN = 0
    WOMAN = 1


@enum.unique
class Ordinal(enum.Enum):
    """Enumeration of all 4 directions."""
    EAST = 0
    NORTH = 1
    WEST = 2
    SOUTH = 3


@enum.unique
class WalkAnimation(enum.Enum):
    """Enumeration of all possible walking animation keyframes."""
    LEFT = 0
    REST = 1
    RIGHT = 2


def walk_animation_cycle():
    """Coherent cycle for the walking animation."""
    while True:
        yield WalkAnimation.LEFT
        yield WalkAnimation.REST
        yield WalkAnimation.RIGHT
        yield WalkAnimation.REST
