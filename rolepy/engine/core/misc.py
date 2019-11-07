import math
from rolepy.engine.core.enums import Ordinal
from rolepy.engine.core.structs import Position


def direction_gradient(ordinal):
    """Return the vector representation of a direction, as a gradient of
       position in this direction.
    """
    if ordinal == Ordinal.NORTH:
        return Position(0, -1)
    if ordinal == Ordinal.SOUTH:
        return Position(0, 1)
    if ordinal == Ordinal.WEST:
        return Position(-1, 0)
    return Position(1, 0)


def reverse_direction(ordinal):
    """Return the opposite of a direction."""
    return {
        Ordinal.NORTH: Ordinal.SOUTH,
        Ordinal.SOUTH: Ordinal.NORTH,
        Ordinal.WEST: Ordinal.EAST,
        Ordinal.EAST: Ordinal.WEST
    }[ordinal]


def front_position(start, direction, distance=1):
    """Return the position that is at a given distance in a given direction
       from a starting position.
    """
    return start + distance * direction_gradient(direction)


def angle_direction(angle):
    """Return the ordinal a vector is pointing to, given its angle."""
    if math.pi / 4 >= angle > -math.pi / 4:
        return Ordinal.EAST
    if 3 * math.pi / 4 >= angle > math.pi / 4:
        return Ordinal.SOUTH
    if -math.pi / 4 >= angle > -3 * math.pi / 4:
        return Ordinal.NORTH
    return Ordinal.WEST
