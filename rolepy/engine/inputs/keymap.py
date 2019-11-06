from rolepy.engine.inputs import Command
import pygame.locals


class Keymap(dict):

    def __init__(self):
        super(Keymap, self).__init__()
        self[Command.MOVE_UP] = pygame.locals.K_z
        self[Command.MOVE_DOWN] = pygame.locals.K_s
        self[Command.MOVE_LEFT] = pygame.locals.K_q
        self[Command.MOVE_RIGHT] = pygame.locals.K_d
        self[Command.RUN] = pygame.locals.K_LSHIFT
        self[Command.HUD] = pygame.locals.K_F1
        self[Command.QUIT] = pygame.locals.K_ESCAPE
        self[Command.INTERACT] = pygame.locals.K_e
