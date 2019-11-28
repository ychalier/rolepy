Inputs module
=============

The inputs module is made of three components:

 - a list of ``Command`` that the user can execute,
 - a ``KeyMap`` that links those commands to actual key inputs that the player can trigger,
 - an ``InputManager`` that detect and execute the commands that the player triggered.

The input manager method ``update`` is called within the main game loop, and
checks for PyGame events. It also contains the logics to decide what action to
take after a given command, depending on the current game state (e.g.
directionnal keys are used to move the player unless a dialogue with answers
is shown).
