import enum


@enum.unique
class EntityState(enum.Enum):

    IDLE = 0
    MOVING = 1
    INTERACTING = 2
