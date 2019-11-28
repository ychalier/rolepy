from rolepy.engine.events import Event
from rolepy.engine.events.enums import EventType


class DialogCloseEvent(Event):

    def __init__(self):
        Event.__init__(self, EventType.DIALOG_CLOSE)
