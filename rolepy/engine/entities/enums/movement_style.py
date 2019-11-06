import enum


@enum.unique
class MovementStyle(enum.Enum):

    STATIC = 0
    RANDOM = 1
    FOLLOW = 2
