from rolepy.model import Item


class ArmorPiece(Item):

    def __init__(self, name, price, defense, slot):
        Item.__init__(self, name, price)
        self.defense = defense
        self.slot = slot
