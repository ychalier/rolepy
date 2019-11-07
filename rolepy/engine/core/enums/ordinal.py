import enum


@enum.unique
class Ordinal(enum.Enum):
    """Enumeration of all 4 directions."""
    EAST = 0
    NORTH = 1
    WEST = 2
    SOUTH = 3
