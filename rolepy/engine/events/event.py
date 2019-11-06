class Event:
    """Basic event class."""

    def __init__(self, event_type, **kwargs):
        self.type = event_type
        for arg_name, arg_value in kwargs.items():
            setattr(self, arg_name, arg_value)

    def __hash__(self):
        return self.type.value

    def __eq__(self, other):
        return self.type == other.type

    def __str__(self):
        return "<%s>" % self.__class__.__name__
