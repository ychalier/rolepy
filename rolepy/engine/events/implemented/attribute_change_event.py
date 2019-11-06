from rolepy.engine.events import Event
from rolepy.engine.events.enums import EventType


class AttributeChangeEvent(Event):
    """Event that are bound to an attribute value."""

    def __init__(self, attribute_name):
        self.attribute_name = attribute_name
        Event.__init__(self, EventType.ATTRIBUTE_CHANGE)

    def __hash__(self):
        return EventType.ATTRIBUTE_CHANGE.value

    def __eq__(self, other):
        if not Event.__eq__(self, other):
            return False
        return self.attribute_name == other.attribute_name

    def __str__(self):
        return "<%s: %s>" % (self.__class__.__name__, self.attribute_name)
