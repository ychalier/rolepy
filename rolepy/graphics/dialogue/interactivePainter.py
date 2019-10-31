import pygame
import numpy as np

class InteractivePainter:
    """Manage Text Interactivity"""

    def __init__(self, drawing_surf):
        self.drawing_surf = drawing_surf

        (self.width, self.height) = drawing_surf.get_size()

        self.current_text = ""
        self.labels = []
        self.heights = []

        """TODO : Font and color should be arguments"""
        self.font = pygame.font.SysFont("consolas", 20)
        self.color = (0, 0, 0)
        self.line_space = 20

    def display_text(self, text):
        """Handle incoming text for the dialog box"""
        i = 0
        while (i < len(text)):
            if (self.font.size(self.current_text + text[i])[0] >= self.width):
                label = self.font.render(self.current_text,
                                         True,
                                         self.color)
                self.labels.append(label)
                self.heights.append(label.get_size()[1])
                if np.sum(self.heights) > self.height:
                    self.labels.pop(0)
                    self.heights.pop(0)

                self.current_text = ""
            self.current_text += text[i]
            i += 1

        current_label = self.font.render(self.current_text,
                                         True,
                                         self.color)
        current_height = current_label.size()[1]

        if np.sum(self.heights) + current_height > self.height:
            self.labels.pop(0)
            self.heights.pop(0)

        display_height = 0
        for i in range(len(self.labels)):
            self.drawing_surf.blit(self.labels[i],
                                   (0, display_height))
            display_height += self.heights[i]

        self.drawing_surf.blit(current_label,
                               (0, display_height + current_height))
