import pygame


class Label:
    """Textual component for an interface."""

    def __init__(self, font, width, height, **kwargs):
        self.font = font
        self.width = width
        self.height = height
        self.align = "center"
        self.color = (255, 255, 255)
        self.background = (0, 0, 0, 100)
        for arg_name, arg_value in kwargs.items():
            setattr(self, arg_name, arg_value)
        self.surface = pygame.Surface(
            (width, height),
            flags=pygame.SRCALPHA | pygame.HWSURFACE,
            depth=32
        )
        self.text = ""

    def update(self, text):
        """Update the text of the label."""
        text = text.strip()
        if text == self.text:
            return
        if text == "":
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
