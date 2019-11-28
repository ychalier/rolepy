import pygame
from rolepy.engine.core.structs import Position
from rolepy.engine.interface.dialogs import DialogBox


class ChoiceBox(DialogBox):

    def __init__(self, manager, answers, **kwargs):
        DialogBox.__init__(self, manager, **kwargs)
        self.surfaces = list()
        self.selection = 0
        self.build_text_lines(answers)
        self.create_surfaces()
        self.build_foreground()

    def build_text_lines(self, answers):
        font = self.manager.fonts[self.settings["font"]]
        width, height = 0, 0
        for answer in answers:
            surface = font.render(
                answer["text"], True, self.settings["text_color"])
            w, h = surface.get_size()
            self.surfaces.append(surface)
            width = max(width, w)
            height += h
        self.settings["width"] = 2 * self.settings["padding"] + \
            2 * self.settings["border_size"] + width
        self.settings["height"] = 2 * self.settings["padding"] + \
            2 * self.settings["border_size"] + height

    def build_foreground(self):
        self.foreground.fill((0, 0, 0, 0))
        cursor = Position(
            self.settings["border_size"] + self.settings["padding"],
            self.settings["border_size"] + self.settings["padding"],
        )
        for i, surface in enumerate(self.surfaces):
            if i == self.selection:
                rect = surface.get_rect()
                rect.top = cursor.y
                rect.left = cursor.x
                pygame.draw.rect(
                    self.foreground, self.settings["highlight_color"], rect)
            self.foreground.blit(surface, cursor.pair())
            cursor.y += surface.get_size()[1]

    def position(self, anchor, text_box):
        return DialogBox.position(self, anchor) + Position(
            text_box.settings["width"] // 2 -
            self.settings["width"] // 2 - self.settings["width"] % 2,
            -text_box.settings["height"]
        )

    def select_up(self):
        self.selection = max(0, self.selection - 1)

    def select_down(self):
        self.selection = min(len(self.surfaces) - 1, self.selection + 1)
