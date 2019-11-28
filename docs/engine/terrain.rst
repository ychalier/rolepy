Terrain module
==============

This modules takes terrain reresentation model as input and creates PyGames
surfaces that can be shown on screen.

World Surfaces
--------------

A ``WorldSurface`` is a finite square portion of the terrain. It extends the
basic PyGame surface class and implements a method to blit terrain tiles on
itself, given a world model representation.

The concerned terrain portion is determined by the ``center`` attribute, around
which we consider a square of tiles. Tiles within that window are blitted to
the surface. If necessary, the **model terrain generation method** is called to
generate the needed tiles.

To fasten its building process, one can use the ``build_from`` method with
an overlapping ``WorldSurface`` as argument. The overlapping part will be
directly blitted to the new surface, without making new queries to the world
model.

World Surfaces Manager
----------------------

The ``WorldSurfaceManager`` uses several ``WorldSurface`` to ensure it always
have the correct one (i.e. the one the player is onto) to display.

To do so, it stores a 3\*3 grid of surfaces. The middle one is supposed to be
centered on the player. When the player moves and reaches the surface limit
(or is close enough that next move would show the surface limit on screen),
the manager **switches** surfaces, so that the middle surface still contains
the player.

To avoid switching too much when the player spends time next to the surface
limit, surfaces **overlap**. That allows for faster building of newer surfaces
(see previous section), and only one surface needs to be displayed at a time.

The proper switch is done by the ``SwitchWorldSurface`` background task.
It either shifts the rows of the columns of the 3\*3 surfaces grid, so that
the correct surface occupies the center. Re-usable surfaces are kept without
being rebuilt. New surfaces are built with the help of overlapping exising ones.

**This process still is not ideal and suffer lag spikes.**
