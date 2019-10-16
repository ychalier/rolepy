from rolepy.model import Item


class Weapon(Item):

    def __init__(self, name, damages):
        Item.__init__(self, name)
        self.damages = damages
