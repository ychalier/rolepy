from rolepy.model.player import Inventory
from rolepy.model.player import Skillset


class Player:

    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.skills = Skillset()
        self.inventory = Inventory()
