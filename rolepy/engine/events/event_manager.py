from rolepy.engine.events import EventListener


class EventManager:
    """Manages events and event listeners."""

    def __init__(self):
        self.listeners = dict()

    def add_event_listener(self, target, event, callback):
        """Register a new event listener."""
        event_listener = EventListener(target, event, callback)
        self.listeners.setdefault(target, dict())
        self.listeners[target].setdefault(event, list())
        self.listeners[target][event].append(event_listener)
        return event_listener

    def provoke(self, target, event, **kwargs):
        """If the target on which the event occured was listening, then call the
           callback from the event listener.
        """
        for event_listener in self.listeners.get(target, dict()).get(event, list()):
            event_listener(**kwargs)
