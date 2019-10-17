class Interface:

    def __init__(self, manager):
        self.manager = manager
        self.boxes = dict()


    def blit(self, screen):
        for position, box in self.boxes.items():
            screen.blit(box.surface, position.pair())
