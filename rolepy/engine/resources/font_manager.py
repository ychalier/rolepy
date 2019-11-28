import pygame


class FontManager(dict):

    def load(self):
        self["consolas12"] = pygame.font.SysFont("consolas", 12)
        self["consolas20"] = pygame.font.SysFont("consolas", 20)
        self["inconsolata20"] = pygame.font.SysFont("inconsolataforpowerline", 20)
