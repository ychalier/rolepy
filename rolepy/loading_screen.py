import time
import random
import threading
import pygame
from rolepy.engine.core.globals import SPRITE_SIZE


class LoadingScreen(threading.Thread):
    """Standalone laoding screen class."""

    def __init__(self, screen, steps, **kwargs):
        threading.Thread.__init__(self)
        self.screen = screen
        self.steps = steps
        self.sub_steps = 0
        self.sub_progress = 0
        self.progress = 0
        self.title = None
        self.sub_title = None
        width, height = self.screen.get_size()
        self.width = width
        self.height = height
        self.background_pattern = pygame.Surface(
            (SPRITE_SIZE, SPRITE_SIZE),
            flags=pygame.SRCALPHA | pygame.HWSURFACE,
            depth=32
        )
        self.background = pygame.Surface(
            (self.width, self.height),
            flags=pygame.SRCALPHA | pygame.HWSURFACE,
            depth=32
        )
        self.font_large = pygame.font.SysFont("ubuntumono", 20)
        self.font_small = pygame.font.SysFont("ubuntumono", 16)
        self.settings = {
            "background_base_color": (51, 105, 30),
            "stripes_color": (0, 61, 0),
            "color_shift_radius": 2,
            "text_color": (255, 255, 255),
            "bar_width": .75,
            "bar_height": 20,
            "bar_margin": 8,
        }
        for key, value in kwargs.items():
            self.settings[key] = value
        self.build_background()

    def build_background(self):
        """Create the background surface of the loading screen, with some
           generated pattern and man-made graphical elements.
        """
        for i in range(SPRITE_SIZE):
            for j in range(SPRITE_SIZE):
                color = list()
                for k in range(3):
                    color.append(min(
                        255,
                        max(
                            0,
                            self.settings["background_base_color"][k]\
                            + random.randint(
                                -self.settings["color_shift_radius"],
                                self.settings["color_shift_radius"]
                            )
                        )
                    ))
                pygame.draw.line(self.background_pattern, color, (i, j), (i, j))
        for k in range(random.randint(1, 2)):
            slope = random.choice([1, -1])
            cursor = [0, 0]
            def mod(cursor):
                return [
                    int(cursor[0]) % SPRITE_SIZE,
                    int(cursor[1]) % SPRITE_SIZE,
                ]
            for _ in range(int(SPRITE_SIZE) + 1):
                pygame.draw.line(
                    self.background_pattern,
                    self.settings["stripes_color"],
                    mod(cursor), mod(cursor)
                )
                cursor[0] += 1
                cursor[1] += slope
        for i in range(0, self.width + SPRITE_SIZE, SPRITE_SIZE):
            for j in range(0, self.height + SPRITE_SIZE, SPRITE_SIZE):
                self.background.blit(self.background_pattern, (i, j))
        rect = pygame.Rect(
            int(.5 * self.width * (1 - self.settings["bar_width"])),
            self.height // 2 - self.settings["bar_height"] // 2,
            int(self.width * self.settings["bar_width"]),
            self.settings["bar_height"]
        )
        pygame.draw.rect(self.background, self.settings["text_color"], rect)
        rect = pygame.Rect(
            int(.5 * self.width * (1 - self.settings["bar_width"])) + 1,
            self.height // 2 - self.settings["bar_height"] // 2 + 1,
            int(self.width * self.settings["bar_width"]) - 2,
            self.settings["bar_height"] - 2
        )
        pygame.draw.rect(self.background, self.settings["background_base_color"], rect)

    def blit(self):
        """Blits background and foreground elements onto the screen."""
        self.screen.blit(self.background, (0, 0))
        if self.title is not None:
            self.screen.blit(self.title, (
                self.width // 2 - self.title.get_size()[0] // 2,
                self.height // 2 - self.title.get_size()[1]\
                 - self.settings["bar_margin"] - self.settings["bar_height"] // 2
            ))
        if self.sub_title is not None:
            self.screen.blit(self.sub_title, (
                self.width // 2 - self.sub_title.get_size()[0] // 2,
                self.height // 2 + self.settings["bar_margin"] + self.settings["bar_height"] // 2
            ))
        progress = 0
        sub_progress = 0
        if self.steps > 0:
            progress = self.progress / self.steps
        if self.sub_steps > 0 and self.steps > 0:
            sub_progress = self.sub_progress / self.sub_steps / self.steps
        progress += sub_progress
        rect = pygame.Rect(
            int(.5 * self.width * (1 - self.settings["bar_width"])),
            self.height // 2 - self.settings["bar_height"] // 2,
            int(self.width * self.settings["bar_width"] * progress),
            self.settings["bar_height"]
        )
        pygame.draw.rect(self.screen, self.settings["text_color"], rect)
        pygame.display.flip()

    def done_step(self):
        """Indicate the loading screen that the current step is done."""
        self.progress += 1

    def done_sub_step(self):
        """Indicate the loading screen that the current sub step is done."""
        self.sub_progress += 1

    def next_step(self, title, sub_steps=0):
        """Switch to the next step, reset sub steps and create new title surface."""
        self.title = self.font_large.render(title, True, self.settings["text_color"])
        self.sub_steps = sub_steps
        self.sub_title = None
        self.sub_progress = 0
        self.blit()

    def next_sub_step(self, sub_title):
        """Switch to the next substep."""
        self.sub_title = self.font_small.render(sub_title, True, self.settings["text_color"])
        self.blit()

    def run(self):
        """Main thread loop."""
        while self.progress < self.steps:
            time.sleep(.01)
