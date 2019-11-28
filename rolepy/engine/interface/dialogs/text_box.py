import time
import pygame
from rolepy.engine.core.structs import Position
from rolepy.engine.core.tasks import AsyncTask
from rolepy.engine.interface.dialogs import DialogBox


class BuildForegroundTask(AsyncTask):

    def __init__(self, text_box):
        def function():
            text_box.async_build_foreground()
        AsyncTask.__init__(self, function)


class TextBox(DialogBox):

    def __init__(self, manager, content, **kwargs):
        DialogBox.__init__(self, manager, **kwargs)
        self.content = content
        self.index = 0
        self.characters = dict()
        self.line_height = 0
        self.char_width = 0
        self.build_characters()
        self.create_surfaces()

    def has_finished(self):
        return self.index >= len(self.content)

    def build_characters(self):
        font = self.manager.fonts[self.settings["font"]]
        for char in set(self.content + " "):
            if char != "\n":
                surface = font.render(char, True, self.settings["text_color"])
                width, height = surface.get_size()
                self.char_width = max(self.char_width, width)
                self.line_height = max(self.line_height, height)
                self.characters[char] = surface

    def async_build_foreground(self):
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
            pygame.draw.polygon(self.foreground, self.settings["text_color"], [
                (self.settings["width"] - margin - 20,
                 self.settings["height"] - margin - 15),
                (self.settings["width"] - margin - 10,
                 self.settings["height"] - margin - 10),
                (self.settings["width"] - margin - 20,
                 self.settings["height"] - margin - 5),
            ])
        self.manager.check_choices_display()

    def build_foreground(self):
        BuildForegroundTask(self).start()
