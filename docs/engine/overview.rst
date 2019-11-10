Overview
========

.. _Pygame: https://www.pygame.org/news

RolePy's game engine is an original creation, solely relying on basic Pygame_'s mechanics. It is currently divided into eight modules, that cover the elementary components of the game implementation. This includes common variables and enumerations, basic data structures, generic classes to represent elements of the game and manager classes that can be used to interact with the engine.

The purpose of this engine is not to serve for the development of other games, therefore it does not need to be too customizable. The split between the engine development and the game development simply allows for a more structured and manageable development progress.

Engine Modules
--------------

The :ref:`core module` contains the basic tools of the engine, the data structures common to all other modules, common utility functions as well as the ``TaskManager``, which handles all the asynchronous tasks that are executed on other threads than the main loop.

The :ref:`resources module` makes the interfaces between the binary resources of the game and the game. It loads them and organize them so they can be easily retrieved later on. Those resources are currently only sprites, but will be extended with sounds and music.

The :ref:`terrain module` takes as input the `scene graph <https://en.wikipedia.org/wiki/Scene_graph>`_ of the game world, and ouputs a surface that can be rendered on the screen. It also handles the loading and unloading of those surfaces into memory, so that there is no loading screen while the player moves around the world.

The :ref:`events module` provides the means for the triggering of various in-game events, such as an attribute changing of value, or an interaction being initiated between the player and an NPC, and the call of appropriate asynchronous callbacks.

The :ref:`inputs module` aims at providing the interface between the player input (currently, the keyboard only) and the game, by binding specific commands to an input key and executing the commands when detected in game.

The :ref:`interface module` handles the representation and the display of the user interface, textual information, dialogues, inventory management, etc.

The :ref:`entities module` handles the representation of the entities in the game. Entities are for example NPCs. While terrain is static and dense, entities are dynamic and sparse; thus they are represented differently. Furthermore, this module provides the mechanics to implement an artificial intelligence for those entities, which will determine their autonomous behavior and their reaction to the player actions.

The :ref:`graphics module` contains the rendering procedures that gather surfaces provided by the different modules and effectively display them on the screen.

Upcoming Features
-----------------

- Add serialization of game current state for saving/loading the game
- Add a module for the specific representation of *structures*
- Fasten the terrain rendering, as ``WorldSurface`` current switch causes noticeable lag spikes
- Load resources as a single sprite sheet
- Add support for animated textures
- Add rendering graphical effects (blurry, day / night, etc.)
- Add advanced interface display (e.g. mouse-controlled inventory management) and animations

More features may be developped as they occur to be needed during the actual game development.
