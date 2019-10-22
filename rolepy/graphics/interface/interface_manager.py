import pygame
from rolepy.graphics.interface import DebugInterface


class InterfaceManager:
    """Manage multiple interfaces and interface resources."""

    EMPTY = 0
    DEBUG_INTERFACE = 1

    def __init__(self, resolution):
        self.state = InterfaceManager.DEBUG_INTERFACE
        self.resolution = resolution
        self.fonts = dict()
        self.interfaces = {InterfaceManager.EMPTY: None}

    def __getitem__(self, key):
        return self.interfaces[key]

    def load(self):
        """Load fonts and build interfaces."""
        self.fonts["consolas"] = pygame.font.SysFont("consolas", 12)
        self.interfaces[InterfaceManager.DEBUG_INTERFACE] = \
            DebugInterface(self)

    def blit(self, screen):
        """Blit current interface to the screen."""
        interface = self.interfaces.get(self.state, None)
        if interface is not None:
            interface.blit(screen)

    def increment_state(self):
        """Switch the currently displayed interface."""
        if self.state == InterfaceManager.EMPTY:
            self.state = InterfaceManager.DEBUG_INTERFACE
        else:
            self.state = InterfaceManager.EMPTY
