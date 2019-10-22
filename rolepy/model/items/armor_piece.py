from rolepy.model.items import Item


class ArmorPiece(Item):
    """Model of an armor piece."""

    def __init__(self, name, price, defense, slot):
        Item.__init__(self, name, price)
        self.defense = defense
        self.slot = slot
