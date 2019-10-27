import threading


class EventListener:
    """Data structure to store an event listener."""

    def __init__(self, target, event, callback):
        self.target = target
        self.event = event
        self.callback = callback

    def __call__(self, *args, **kwargs):
        arguments = {
            "listener": self,
            "positional": args,
            "keywords": kwargs
        }
        thread = threading.Thread(target=self.callback, args=(arguments,))
        thread.start()