Events module
=============

The events module handles the emission and resolution of messages with a
JavaScript-like sysytem.

First, ``EventListener`` objects are instanciated on a target with a callback
function, and stored in the ``EventManager``.

When an event occur, the code executing it uses the ``provoke`` method of the
``EventManager``, specifying the target of the event. If the manager finds an
event listener corresponding to that event and that target, it spawns a
thread in which the attached callback is executed.
