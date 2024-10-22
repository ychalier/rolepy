from rolepy.engine.core.structs import Position
from rolepy.engine.interface.dialogs import TextBox
from rolepy.engine.interface.dialogs import ChoiceBox
from rolepy.engine.events.implemented import DialogCloseEvent
from rolepy.engine.events.implemented import TriggerEvent


class DialogManager:
    """Handle the currently displayed dialog box."""

    def __init__(self, interface_manager):
        self.interface_manager = interface_manager
        self.fonts = self.interface_manager.fonts
        self.entity = None
        self.answers = None
        self.text_box = None
        self.choice_box = None
        self.is_displayed = False
        self.show_choices = False
        self.position = Position(0, 0)

    def open_dialog(self, entity, position, content, answers):
        """Initiate the display of a dialog box."""
        self.entity = entity
        self.text_box = TextBox(self, content)
        self.choice_box = ChoiceBox(self, answers, margin_bottom=1)
        self.answers = answers
        self.position = position
        self.is_displayed = True
        self.validate()

    def blit(self, screen, transformer):
        """Blit the current dialog boxes to the screen."""
        if not self.is_displayed:
            return
        tpos = self.text_box.position(transformer(self.position + Position(.5, 0)), "middle-above")
        screen.blit(self.text_box.background, tpos.pair())
        screen.blit(self.text_box.foreground, tpos.pair())
        if self.show_choices:
            cpos = self.choice_box.position(
                tpos + Position(self.text_box.settings["width"], 0),
                "right-above"
            )
            screen.blit(self.choice_box.background, cpos.pair())
            screen.blit(self.choice_box.foreground, cpos.pair())

    def validate(self):
        """Handle validation event from user input."""
        if not self.text_box.has_finished():
            self.text_box.build_foreground()
        else:
            self.interface_manager.game.event_manager.provoke(self.entity, DialogCloseEvent())
            if self.show_choices:
                self.interface_manager.game.event_manager.provoke(
                    self.entity,
                    TriggerEvent(self.answers[self.choice_box.selection]["trigger"]),
                )
            self.is_displayed = False
            self.show_choices = False
            del self.text_box
            self.text_box = None
            del self.choice_box
            self.choice_box = None

    def cancel(self):
        """Handle cancellation event from user input."""
        self.is_displayed = False
        self.show_choices = False
        del self.text_box
        self.text_box = None
        del self.choice_box
        self.choice_box = None

    def check_choices_display(self):
        """Check if choice box should be displayed."""
        if self.text_box is not None\
                and self.text_box.has_finished()\
                and self.choice_box is not None\
                and len(self.choice_box.surfaces) > 0:
            self.show_choices = True
