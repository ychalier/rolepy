import time
import pygame
from rolepy.engine.core.structs import Position
from rolepy.engine.core.tasks import AsyncTask
from rolepy.engine.interface.dialogs import DialogBox


class BuildForegroundTask(AsyncTask):
    """Thread dedicated to blitting text on the foreground."""

    def __init__(self, text_box):
        def function():
            text_box.async_build_foreground()
        AsyncTask.__init__(self, function)


class TextBox(DialogBox):
    """Dialog box that displays large text portions."""

    def __init__(self, manager, content, **kwargs):
        DialogBox.__init__(self, manager, **kwargs)
        self.content = content
        self.index = 0
        self.characters = dict()
        self.line_height = 0
        self.char_width = 0
        self.in_animation = False
        self.build_characters()
        self.create_surfaces()

    def has_finished(self):
        """Return true if all text has been displayed."""
        return self.index >= len(self.content)

    def build_characters(self):
        """Build a small surface for each distinct character in the text."""
        font = self.manager.fonts[self.settings["font"]]
        for char in set(self.content + " "):
            if char != "\n":
                surface = font.render(char, True, self.settings["text_color"])
                width, height = surface.get_size()
                self.char_width = max(self.char_width, width)
                self.line_height = max(self.line_height, height)
                self.characters[char] = surface

    def async_build_foreground(self):
        """Actual foreground building method, that needs to be executed asynchronously
           to allow for char-by-char blitting animation.
        """
        self.in_animation = True
        self.foreground.fill((0, 0, 0, 0))
        margin = self.settings["border_size"] + self.settings["padding"]
        cursor = Position(margin, margin)
        while self.index < len(self.content):
            char = self.content[self.index]
            word = 0
            for j in range(self.index, len(self.content)):
                c = self.content[j]
                if c not in [" ", "\n"]:
                    word += 1
                else:
                    break
            if char == "\n" or\
                    cursor.x > self.settings["width"] - margin - word * self.char_width:
                cursor.y += self.line_height
                cursor.x = margin
            if cursor.y > self.settings["height"] - margin - self.line_height:
                break
            if char != "\n":
                surface = self.characters[char]
                self.foreground.blit(surface, cursor.pair())
                cursor.x += surface.get_size()[0]
                if self.settings["delay"] > 0:
                    time.sleep(self.settings["delay"])
            self.index += 1
        if not self.has_finished():
            length = 8
            h_length = length * .5 * (3 ** .5)
            org = Position(
                self.settings["width"] - margin,
                self.settings["height"] - margin
            )
            pygame.draw.polygon(self.foreground, self.settings["text_color"], [
                (org - Position(h_length, length)).pair(),
                (org - Position(0, .5 * length)).pair(),
                (org - Position(h_length, 0)).pair(),
            ])
        self.manager.check_choices_display()
        self.in_animation = False

    def build_foreground(self):
        """Public method to trigger the foreground blitting."""
        BuildForegroundTask(self).start()
