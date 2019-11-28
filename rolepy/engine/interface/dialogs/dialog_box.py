import pygame
from rolepy.engine.core.misc import draw_rounded_rectangle
from rolepy.engine.core.structs import Position


class DialogBox:
    """Basic class to display a dialog box."""

    def __init__(self, manager, **kwargs):
        self.manager = manager
        self.settings = {
            "width": 200,
            "height": 150,
            "delay": .015,
            "radius": 8,
            "padding": 8,
            "font": "inconsolata20",
            "background_color": (255, 255, 255, 200),
            "border_color": (0, 0, 0),
            "border_size": 2,
            "text_color": (0, 0, 0),
            "highlight_color": (180, 130, 155),
            "margin_bottom": 5,
        }
        for key, value in kwargs.items():
            self.settings[key] = value
        self.background = None
        self.foreground = None

    def create_surfaces(self):
        """Create PyGame surfaces and blit the background."""
        self.background = pygame.Surface(
            (self.settings["width"], self.settings["height"]),
            flags=pygame.SRCALPHA | pygame.HWSURFACE,
            depth=32
        )
        self.foreground = pygame.Surface(
            (self.settings["width"], self.settings["height"]),
            flags=pygame.SRCALPHA | pygame.HWSURFACE,
            depth=32
        )
        self.build_background()

    def build_background(self):
        """Blit rounded rectangles to the background surface."""
        self.background.fill((0, 0, 0, 0))
        draw_rounded_rectangle(
            self.background,
            0,
            self.settings["width"],
            self.settings["height"],
            self.settings["radius"],
            self.settings["border_color"],
        )
        draw_rounded_rectangle(
            self.background,
            self.settings["border_size"],
            self.settings["width"] - 2 * self.settings["border_size"],
            self.settings["height"] - 2 * self.settings["border_size"],
            self.settings["radius"],
            self.settings["background_color"],
        )

    def position(self, anchor, location):
        """Return the position of the top left corner of the box relative to
           a given anchor.
        """
        if location == "middle-above":
            return anchor - Position(
                self.settings["width"] // 2,
                self.settings["height"] + self.settings["margin_bottom"]
            )
        if location == "right-above":
            return anchor - Position(
                self.settings["width"],
                self.settings["height"] + self.settings["margin_bottom"]
            )
        return anchor
