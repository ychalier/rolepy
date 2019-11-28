from rolepy.engine.events import Event
from rolepy.engine.events.enums import EventType


class DialogCloseEvent(Event):
    """Event triggered by the dialog manager to notify of the end of an interaction."""

    def __init__(self):
        Event.__init__(self, EventType.DIALOG_CLOSE)
