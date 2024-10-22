from rolepy.engine.core.structs import Position
from rolepy.engine.core.globals import SPRITE_SIZE


class Camera(Position):
    """Custom position class with animation methods to represent the camera that
       renders the world.
    """

    def __init__(self):
        Position.__init__(self, 0, 0)

    def smooth_translation(self, destination):
        """Make a step in the smooth transition from current position to the
           destination.
        """
        gap = destination - self
        if gap.norm() < .1 / SPRITE_SIZE:
            self.x = destination.x
            self.y = destination.y
        self.x = .01 * (99. * self.x + destination.x)
        self.y = .01 * (99. * self.y + destination.y)
