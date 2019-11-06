from rolepy.engine.core.enums import Ordinal
from rolepy.engine.core.structs import Position
import math


def direction_gradient(ordinal):
    if ordinal == Ordinal.NORTH:
        return Position(0, -1)
    if ordinal == Ordinal.SOUTH:
        return Position(0, 1)
    if ordinal == Ordinal.WEST:
        return Position(-1, 0)
    return Position(1, 0)


def reverse_direction(ordinal):
    return {
        Ordinal.NORTH: Ordinal.SOUTH,
        Ordinal.SOUTH: Ordinal.NORTH,
        Ordinal.WEST: Ordinal.EAST,
        Ordinal.EAST: Ordinal.WEST
    }[ordinal]


def front_position(start, direction, distance=1):
    return start + distance * direction_gradient(direction)


def angle_direction(angle):
    if math.pi / 4 >= angle > -math.pi / 4:
        return Ordinal.EAST
    elif 3 * math.pi / 4 >= angle > math.pi / 4:
        return Ordinal.SOUTH
    elif -math.pi / 4 >= angle > -3 * math.pi / 4:
        return Ordinal.NORTH
    return Ordinal.WEST
