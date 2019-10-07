class Position:

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

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)

    def __rmul__(self, other):
        return Position(other * self.x, other * self.y)

    def target(self):
        return Position(round(self.x), round(self.y))

    def remainder(self):
        return self - self.target()

    def pair(self):
        return [self.x, self.y]
