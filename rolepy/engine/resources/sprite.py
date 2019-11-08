import pygame
from rolepy.engine.core.globals import SPRITE_SIZE


class Sprite(pygame.Surface):
    """Square surface showing a sprite loaded from a file."""

    def __init__(self, path):
        pygame.Surface.__init__(
            self,
            (SPRITE_SIZE, SPRITE_SIZE),
            pygame.SRCALPHA | pygame.DOUBLEBUF | pygame.HWSURFACE,
            32
        )
        self.path = path

    def load(self):
        """Load a square sprite and blit it to internal surface."""
        if self.path is not None:
            self.blit(pygame.image.load(self.path).convert_alpha(), (0, 0))
