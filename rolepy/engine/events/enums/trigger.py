import enum


@enum.unique
class Trigger(enum.Enum):
    """Enumeration of possible triggers."""
    RESET = 0
    ANSWER_YES = 1
    ANSWER_NO = 2
    ANSWER_HALT = 3
    ANSWER_RETURN = 4
    ANSWER_CANCEL = 5
