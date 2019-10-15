import pygame


class Interface:

    def __init__(self, resolution):
        self.boxes = dict()
        self.fonts = dict()

    def load(self):
        self.fonts["consolas"] = pygame.font.SysFont("consolas", 12)

    def blit(self, screen):
        for position, box in self.boxes.items():
            screen.blit(box.surface, position.pair())
