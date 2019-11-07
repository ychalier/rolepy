import enum


@enum.unique
class MovementStyle(enum.Enum):
    """Represent the type of autonomous movement of an entity."""
    STATIC = 0
    RANDOM = 1
    FOLLOW = 2
