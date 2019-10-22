class Inventory:
    """Hold the inventory of a character."""

    BAG_SIZE = 10

    def __init__(self):
        self.bag = [None] * Inventory.BAG_SIZE
        self.weapon = None
        self.helmet = None
        self.chest = None
        self.legs = None
        self.boots = None
        self.gloves = None
        self.purse = 0
