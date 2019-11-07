import enum


@enum.unique
class Posture(enum.Enum):
    """Enumeration of all possible postures."""
    LEFT = 0
    REST = 1
    RIGHT = 2
