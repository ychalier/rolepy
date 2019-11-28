import pygame
from rolepy.engine.core.enums import Ordinal
from rolepy.engine.inputs import Command
from rolepy.engine.inputs import Keymap


class InputManager:
    """Handle the inputs of the player and execute the corresponding commands."""

    def __init__(self, game):
        self.game = game
        self.keymap = Keymap()

    def update(self):
        """Handle user input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT \
                    or (event.type == pygame.KEYDOWN and event.key == self.keymap[Command.QUIT]):
                self.game.quit()
            elif event.type == pygame.KEYDOWN:
                if not self.game.interface_manager.dialog_manager.is_displayed and event.key in [
                        self.keymap[Command.MOVE_UP],
                        self.keymap[Command.MOVE_DOWN],
                        self.keymap[Command.MOVE_LEFT],
                        self.keymap[Command.MOVE_RIGHT]]:
                    direction = {
                        self.keymap[Command.MOVE_UP]: Ordinal.NORTH,
                        self.keymap[Command.MOVE_DOWN]: Ordinal.SOUTH,
                        self.keymap[Command.MOVE_LEFT]: Ordinal.WEST,
                        self.keymap[Command.MOVE_RIGHT]: Ordinal.EAST,
                    }[event.key]
                    self.game.task_manager.start(
                        self.game.entity_manager.player.move(
                            direction, 1, True),
                        log=False
                    )
                elif event.key == self.keymap[Command.RUN]:
                    self.game.entity_manager.player.attributes.set("speed", 10)
            elif event.type == pygame.KEYUP:
                if event.key == self.keymap[Command.RUN]:
                    self.game.entity_manager.player.attributes.set("speed", 5)
                elif event.key == self.keymap[Command.HUD]:
                    self.game.interface_manager.increment_state()
                elif event.key == self.keymap[Command.INTERACT]:
                    if self.game.interface_manager.dialog_manager.is_displayed:
                        if not self.game.interface_manager.dialog_manager.text_box.in_animation:
                            self.game.interface_manager.dialog_manager.validate()
                    else:
                        self.game.entity_manager.detect_interaction()
                elif self.game.interface_manager.dialog_manager.is_displayed and self.game.interface_manager.dialog_manager.show_choices and event.key in [
                        self.keymap[Command.MOVE_UP],
                        self.keymap[Command.MOVE_DOWN]]:
                    if event.key == self.keymap[Command.MOVE_UP]:
                        self.game.interface_manager.dialog_manager.choice_box.select_up()
                    elif event.key == self.keymap[Command.MOVE_DOWN]:
                        self.game.interface_manager.dialog_manager.choice_box.select_down()
                    self.game.interface_manager.dialog_manager.choice_box.build_foreground()
