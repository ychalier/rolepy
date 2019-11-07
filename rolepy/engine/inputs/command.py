import enum


@enum.unique
class Command(enum.Enum):
    """List possible commands that a player can input."""
    MOVE_UP = 0
    MOVE_DOWN = 1
    MOVE_LEFT = 2
    MOVE_RIGHT = 3
    INTERACT = 4
    RUN = 5
    HUD = 6
    QUIT = 7
