from rolepy.engine.events import Event
from rolepy.engine.events.enums import EventType


class TriggerEvent(Event):
    """Event fired when a trigger is emitted, to change an entity intellect state."""

    def __init__(self, trigger):
        Event.__init__(self, EventType.TRIGGER_EVENT)
        self.trigger = trigger

    def __hash__(self):
        return self.trigger.value

    def __eq__(self, other):
        if not Event.__eq__(self, other):
            return False
        return self.trigger == other.trigger
