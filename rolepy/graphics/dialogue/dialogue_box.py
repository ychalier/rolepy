import pygame
import interactivePainter

class DialogueBox:
    """Manage dialogue box, those handle message from the game and dialogue between players."""
    def __init__(self, width, height, screen):
        self.height = height
        self.width = width
        self.surface = pygame.Surface(
            (self.width, self.height),
            pygame.HWSURFACE)
        self.interactivePainter = interactivePainter.InteractivePainter(self.surface)
        self.screen = screen
        

    def update(self, text, j, verbose=True):
        """Update the display of the dialogue box"""
        self.surface.fill((255, 255, 255))
        (width, height) = self.screen.get_size()
        position = (0, height - self.height)

        if j % 100 == 0:
            self.interactivePainter.display_text(text)
        if verbose:
            print('height : ', self.height)
            print('width : ', self.width)
            print('position : ', position)

        self.screen.blit(self.surface, position)

if __name__ == '__main__':
    pygame.init()
    text = 'Bonjour, mon pays est la France.'
    running = True
    width = 300
    height = 300
    screen = pygame.display.set_mode((width, height), pygame.HWSURFACE)
    font = pygame.font.SysFont("consolas", 15)
    #print('text : ', font.metrics(text))
    dialogue_box = DialogueBox(width=width,
                               height=150,
                               screen=screen)
    j = 0
    delay = 100
    while running:
        screen.fill((0, 0, 0))
        dialogue_box.update(text, j)
        j += 1
        event_list = pygame.event.get()
        
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False

        text = text

        pygame.display.flip()


















        
        

        
