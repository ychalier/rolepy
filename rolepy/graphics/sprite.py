import pygame
from rolepy.globals import SPRITE_SIZE


class Sprite(pygame.Surface):

    def __init__(self, path):
        pygame.Surface.__init__(
            self, (SPRITE_SIZE, SPRITE_SIZE), pygame.SRCALPHA, 32)
        self.path = path

    def load(self):
        if self.path is not None:
            self.blit(pygame.image.load(self.path), (0, 0))
