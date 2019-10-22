import math


class Position:
    """2D position vector."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Position(-self.x, -self.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return "Pos(%f, %f)" % (self.x, self.y)

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)

    def __mul__(self, other):
        return Position(self.x * other.x, self.y * other.y)

    def __rmul__(self, other):
        return Position(other * self.x, other * self.y)

    def norm_inf(self):
        """Return the infinite norm of the vector."""
        return max(abs(self.x), abs(self.y))

    def angle(self):
        """Return the argument of the vector as a complex number."""
        vect = complex(self.x, self.y)
        return math.atan2(vect.imag, vect.real)

    def inner_product(self, other):
        """Return the inner product of two vectors."""
        return self.x * other.x + self.y * other.y

    def target(self):
        """Return a new position with rounded coordinates."""
        return Position(round(self.x), round(self.y))

    def remainder(self):
        """Return the floating quantities of the position."""
        return self - self.target()

    def pair(self):
        """Return the position as a list."""
        return [self.x, self.y]

    def round(self):
        """Remove the floating part of the position."""
        self.x = round(self.x)
        self.y = round(self.y)
