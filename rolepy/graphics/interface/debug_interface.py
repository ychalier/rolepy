from rolepy.graphics.interface import Interface
from rolepy.graphics.interface import Label
from rolepy.misc import Position


class DebugInterface(Interface):
    """Default interface showing debugging informations."""

    def __init__(self, manager):
        Interface.__init__(self, manager)
        self.fps = Label(manager.fonts["consolas"], 151, 29)
        self.pos = Label(manager.fonts["consolas"], 151, 29)
        self.zone = Label(manager.fonts["consolas"], 151, 29)
        self.boxes[Position(8, 8)] = self.fps
        self.boxes[Position(8, 45)] = self.pos
        self.boxes[Position(8, manager.resolution[1] - 37)] = self.zone
