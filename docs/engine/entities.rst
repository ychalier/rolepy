Entities module
===============

Entities are instances of the class ``Entity``. They can be non-payable
characters, or abstract game logic elements that the player can interact with.

Entity Attributes
-----------------

All attributes of an entity are stored as attributes of the ``EntityAttributes``
class. This includes the texture, the current position, the speed (in tile per
second), the direction, the posture, etc.

There is a universal **setter** for those attributes, that fires an
``AttributeChangeEvent`` whenever it is called. That way one can bind callbacks
when the player reaches a given position, for instance.

Entity Manager
--------------

The ``EntityManager`` is an attribute of the main game object. It stores the
entities in a **map** called ``EntityManager.entities``, where keys are hashed
positions and value are sets of entities whose position share the same hash.

Currently, the **hashing** of the position only considers the rounded value of
the entity position, i.e. the closest tile to the entity. It has no impact on a
static entity, only matters when it is moving and its position takes floating
values.

The manager keeps a **registry** called ``EntityManager.registry`` of nearby
entities. Its attributes ``width`` and ``height`` define a window centered on
its ``center``, and the registry contains all entities within that window. This
allows for considering only a small set of entities when doing AI operations.
The belonging of one particular entity to the registry can be computed with
the method ``update_entity_position``, which is namely used when the entity
is moving, so we do not have to recompute the whole window.

Artificial Intelligence
-----------------------

Entity AI is handled by the ``Intellect`` class, which namely represents a
finite state automaton. States are ``Behavior`` instances, while transitions
use an alphabet of ``Triggers``, currently:

 - ``Trigger.RESET``
 - ``Trigger.ANSWER_YES``
 - ``Trigger.ANSWER_NO``
 - ``Trigger.ANSWER_HALT``
 - ``Trigger.ANSWER_RETURN``
 - ``Trigger.ANSWER_CANCEL``

The behavior of an entity defines how it reacts to the player interaction and
how it makes autonomous decisions.

The basic entity **state** is ``IDLE``. When interacting with the player, it
becomes ``INTERACTING``. When in movement, it is ``MOVING``. This state allows
to decide what to do given the situation.

Interaction
***********

The behavior contains the text and the answers to show when a dialog is opened
by the player interaction. This interaction is first triggered in the
``InputManager``, and goes trough the ``EntityManager``, which finds the
triggered ``Entity``, which determines its current ``Behavior`` through the
current state of the ``Intellect``.

The ``DialogManager`` handles the display of the text and the interaction with
the player for the answer selection. When it finishes, several events are fired:

 - ``DialogCloseEvent`` to notify that the interaction has ended,
 - ``TriggerEvent`` to notify that an answer has been selected and the
   intellect state must be updated accordingly.

Autonomous Actions
******************

The ``take_action`` methods is called at each iteration of the ``EntityThread``.
For now it only handles the movement style, either staying put, following the
player, going somewhere or wandering.

The ``Movement`` class is an asynchronous task that moves the entity around,
takes care of its posture animation, and early stops the movement if it detects
a collision.
