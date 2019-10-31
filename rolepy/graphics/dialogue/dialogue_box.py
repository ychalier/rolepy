import pygame

class DialogueBox:
    """Manage dialogue box, those handle message from the game and dialogue between players."""
    def __init__(self, width, height, font, color, screen):
        self.height = height
        self.width = width
        self.surface = pygame.Surface(
            (self.width, self.height),
            pygame.HWSURFACE)

        """
        TODO :
        Font and colors should be handled on a message-wise bases
        and therefore should not be attributes ...
        """
        self.font = font
        self.color = color

        self.screen = screen
        

    def update(self, text, verbose=True):
        """Update the text of the dialogue box"""
        print('updating dialogue box')
        self.surface.fill((255, 255, 255))
        (width, height) = self.screen.get_size()

        position = (0, height - self.height)

        if verbose:
            print('height : ', self.height)
            print('width : ', self.width)
            print('position : ', position)

        label = self.font.render(text, True, self.color)
        self.surface.blit(label, (0, 0))

        self.screen.blit(self.surface, position)

if __name__ == '__main__':
    pygame.init()
    text = 'bonjour \n mon pays est la France'
    running = True
    width = 600
    height = 600
    screen = pygame.display.set_mode((width, height), pygame.HWSURFACE)
    font = pygame.font.SysFont("consolas", 10)
    print('text : ', font.metrics(text))
    color = (0, 0, 0)
    dialogue_box = DialogueBox(width=width,
                               height=300,
                               font=font,
                               color=color,
                               screen=screen)
    while running:
        screen.fill((0, 0, 0))
        dialogue_box.update(text)
        event_list = pygame.event.get()
        
        for event in event_list:
            if event.type == pygame.QUIT:
                running = False

        text = text

        pygame.display.flip()


















        
        

        
