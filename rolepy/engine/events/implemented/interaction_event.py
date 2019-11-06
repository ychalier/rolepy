from rolepy.engine.events import Event
from rolepy.engine.events.enums import EventType


class InteractionEvent(Event):

    def __init__(self):
        Event.__init__(self, EventType.INTERACTION_EVENT)
