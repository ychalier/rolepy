import enum


@enum.unique
class EventType(enum.Enum):
    """Enumeration of possible monitorable events."""

    ATTRIBUTE_CHANGE = 0
    KEY_UP = 1


class Event:
    """Basic event class."""

    def __init__(self, event_type, **kwargs):
        self.type = event_type
        for arg_name, arg_value in kwargs.items():
            setattr(self, arg_name, arg_value)


class AttributeChangeEvent(Event):
    """Event that are bound to an attribute value."""

    def __init__(self, attribute_name):
        self.attribute_name = attribute_name
        Event.__init__(self, EventType.ATTRIBUTE_CHANGE)

    def __hash__(self):
        return EventType.ATTRIBUTE_CHANGE.value

    def __eq__(self, other):
        return self.attribute_name == other.attribute_name

    def __str__(self):
        return "<%s: %s>" % (self.__class__.__name__, self.attribute_name)


class KeyUpEvent(Event):
    """Event bound to a key stroke."""

    def __init__(self, key):
        self.key = key
        Event.__init__(self, EventType.KEY_UP)

    def __hash__(self):
        return EventType.KEY_UP.value

    def __eq__(self, other):
        return self.key == other.key

    def __str__(self):
        return "<%s: %s>" % (self.__class__.__name__, self.key)
