from rolepy.model.items import Item


class Weapon(Item):
    """Model for weapons."""

    def __init__(self, name, price, damages):
        Item.__init__(self, name, price)
        self.damages = damages
