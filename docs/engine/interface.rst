Interface module
================

The interface module handles the overlaying labels displaying infos to the
player, as well as dialogs.

Head User Display
-----------------

The ``InterfaceManager`` serves an ``Interface`` to be rendered on the screen.
The severd interface is determined by the ``state`` attribute, which allows
switching from one surface to another.

Interfaces are sets of absolutly positionned ``Label``, that contain textual
information.

Dialogs
-------

The ``DialogBox`` provides basic tools to create and display a box with a
border, a background, and a foreground. The foreground is either multi-panel
text in the ``TextBox``, with an character-by-character blitting animation
happening in a dedicated thread, or several one-line choices in the
``ChoiceBox``, that keeps a ``selection`` attribute depending on which choice
is currently highlighted.

The ``DialogManager`` handles the display of those boxes, one pair at a time.
When the dialog is closed, it fires ``DialogCloseEvent``, and if a choice
has been made through the ``ChoiceBox``, it also fires ``TriggerEvent`` with
the selected trigger.
