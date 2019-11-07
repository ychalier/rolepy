import enum


@enum.unique
class EntityState(enum.Enum):
    """Represent the current computing status of an entity."""
    IDLE = 0
    MOVING = 1
    INTERACTING = 2
