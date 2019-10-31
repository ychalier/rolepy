import pygame

class InteractivePainter:
    """Manage Text Interactivity"""

    def __init__(self, drawing_surf, font, color):
        self.drawing_surf = drawing_surf

        (self.width_limit, self.height_limit) = drawing_surf.get_size() 

        self.current_text = ""
        self.line_space = font.size

        self.current_width = 0
        self.current_height = 0

        self.font = font
        self.color = color
    
    def display_text(self, text):

        
        






        






