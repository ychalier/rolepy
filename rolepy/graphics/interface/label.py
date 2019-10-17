import pygame


class Label:

    def __init__(self, font, width, height, align="center", background=(0, 0, 0, 100), color=(255, 255, 255)):
        self.font = font
        self.align = align
        self.color = color
        self.width = width
        self.height = height
        self.background = background
        self.surface = pygame.Surface((width, height), pygame.SRCALPHA | pygame.HWSURFACE, 32)
        self.text = ""

    def update(self, text):
        text = text.strip()
        if text == self.text:
            return
        elif text == "":
            self.surface.fill((0, 0, 0, 0))
            self.text = ""
            return
        self.text = text
        label = self.font.render(text, True, self.color)
        if self.background is not None:
            self.surface.fill(self.background)
        else:
            self.surface.fill((0, 0, 0, 0))
        position = (0, 0)
        if self.align == "center":
            position = (
                .5 * (self.width - label.get_width()),
                .5 * (self.height - label.get_height())
            )
        self.surface.blit(label, position)
