import pygame
from rolepy.globals import SPRITE_SIZE


class Sprite(pygame.Surface):
    """Square surface showing a sprite loaded from a file."""

    def __init__(self, path):
        pygame.Surface.__init__(
            self, (SPRITE_SIZE, SPRITE_SIZE), pygame.SRCALPHA, 32)
        self.path = path

    def load(self):
        """Load a square sprite and blit it to internal surface."""
        if self.path is not None:
            self.blit(pygame.image.load(self.path), (0, 0))
