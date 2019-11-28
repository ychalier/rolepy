Graphics module
===============

The graphics module holds a class for the ``Camera``, that extends the basic
``Position`` class by giving it a smooth translation method towards a given
destination. That makes the smooth scrolling effect of the in-game camera.

It also contains the ``Render`` class that regroups all surfaces components
from other modules and blit everything to the screen. For that it uses a
``transformer`` function that maps logic model coordinates to actual pixel-based
positions.
