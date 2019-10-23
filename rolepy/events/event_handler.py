import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_LSHIFT, K_ESCAPE, K_F1
from rolepy.globals import Ordinal
from rolepy.events import EventListener
from rolepy.events import KeyUpEvent


class EventHandler:
    """Manages events and event listeners."""

    def __init__(self, game):
        self.game = game
        self.listeners = dict()

    def handle_input_events(self):
        """Handle user input."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT \
                    or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
                self.game.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [K_UP, K_DOWN, K_RIGHT, K_LEFT]:
                    direction = {
                        K_UP: Ordinal.NORTH,
                        K_DOWN: Ordinal.SOUTH,
                        K_LEFT: Ordinal.WEST,
                        K_RIGHT: Ordinal.EAST,
                    }[event.key]
                    self.game.task_manager.start(
                        self.game.player_entity.move(direction, 1, True),
                        log=False
                    )
                elif event.key == K_LSHIFT:
                    self.game.player_entity.set_speed(10)
            elif event.type == pygame.KEYUP:
                if event.key == K_LSHIFT:
                    self.game.player_entity.set_speed(5)
                elif event.key == K_F1:
                    self.game.interface_manager.increment_state()
                self.trigger(self.game, KeyUpEvent(event.key))

    def add_event_listener(self, target, event, callback):
        """Register a new event listener."""
        event_listener = EventListener(target, event, callback)
        self.listeners.setdefault(target, dict())
        self.listeners[target].setdefault(event, list())
        self.listeners[target][event].append(event_listener)
        return event_listener

    def trigger(self, target, event, *args, **kwargs):
        """If the target on which the event occured was listening, then call the
           callback from the event listener.
        """
        for event_listener in self.listeners.get(target, dict()).get(event, list()):
            event_listener(*args, **kwargs)
