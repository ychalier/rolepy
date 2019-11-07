import enum


@enum.unique
class Trigger(enum.Enum):
    """Enumeration of possible triggers."""
    RESET = 0
    ANSWER_YES = 1
    ANSWER_NO = 2
