import enum


@enum.unique
class EventType(enum.Enum):
    """Enumeration of possible monitorable events."""
    ATTRIBUTE_CHANGE = 0
    INTERACTION_EVENT = 1
    TRIGGER_EVENT = 2
