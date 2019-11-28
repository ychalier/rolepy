from rolepy.engine.interface import DebugInterface
from rolepy.engine.interface.dialogs import DialogManager
from rolepy.engine.resources import FontManager


class InterfaceManager:
    """Manage multiple interfaces and interface resources."""

    EMPTY = 0
    DEBUG_INTERFACE = 1

    def __init__(self, game):
        self.state = InterfaceManager.DEBUG_INTERFACE
        self.game = game
        self.resolution = game.settings.resolution
        self.fonts = FontManager()
        self.interfaces = {InterfaceManager.EMPTY: None}
        self.dialog_manager = DialogManager(self)

    def __getitem__(self, key):
        return self.interfaces[key]

    def load(self):
        """Load fonts and build interfaces."""
        self.fonts.load()
        self.interfaces[InterfaceManager.DEBUG_INTERFACE] = \
            DebugInterface(self)

    def blit(self, screen, transformer):
        """Blit current interface to the screen."""
        self.dialog_manager.blit(screen, transformer)
        interface = self.interfaces.get(self.state, None)
        if interface is not None:
            interface.blit(screen)

    def increment_state(self):
        """Switch the currently displayed interface."""
        if self.state == InterfaceManager.EMPTY:
            self.state = InterfaceManager.DEBUG_INTERFACE
        else:
            self.state = InterfaceManager.EMPTY
