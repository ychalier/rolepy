import pygame


class InterfaceBox:

    def __init__(self, interface, width, height):
        self.interface = interface
        self.width = width
        self.height = height
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
        label = self.interface.fonts["consolas"].render(text, True, (255, 255, 255))
        self.surface.fill((0, 0, 0, 100))
        self.surface.blit(label, (
            .5 * (self.width - label.get_width()),
            .5 * (self.height - label.get_height())
        ))
