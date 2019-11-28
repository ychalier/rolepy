Procedural Generation
=====================

Current procedural generation only concerns the terrain. It relies on an
infinite heatmap.

Heatmap Generation
------------------

An heatmap is made of several **chunks**. Each chunk is a fixed size square,
each cell containing a value between -1 and 1. This value is determined
thanks to the
`diamond-square algorithm <https://en.wikipedia.org/wiki/Diamond-square_algorithm>`_.
This algorithm follows a fractal principle, averaging alternating patterns while
introducing smaller and smaller randomness. Results are random yet sensible
distribution of numbers.

Each chunk is determined by its own **seed**, in turn determined by the hash of
its center position.

The **extension** from the chunk to the infinite map is done by imposing
constraints on the algorithm on the borders of the chunks, so that the value
matches the border of the previous chunk. As this would be generation-ordering
dependent, generation order is sort of fixed: when a chunk needs to be
generated, chunks located in the same corner of the map that are closer to
the center need to be generated. This principle propagates recursively to the
center chunk.

Biome Generation
----------------

The world generation uses two heatmaps to determine the biome: a **temperature**
one and a **humidity** one. A given position is classified into a biome
depending on the value of those two heatmaps at that position. The
classification is currently done with the following rules:

.. code-block:: python

    if temperature < -.5 and humidity < 0:
        return Biome.MOUNTAIN
    if temperature > .5 and humidity < -.5:
        return Biome.DESERT
    if humidity > .1:
        return Biome.FOREST
    return Biome.PLAIN

Local Variations
----------------

When going from biome to actual **tile**, one may face a choice among several
tile candidates. For instance, if the biome is plain, then several kinds of
grass can be displayed.

Another **heatmap** is used for that, whose value at a given position is hashed
into a seed for the random choice of the tile variation.

The **hashing function** used to this matter first applies a multiplication
factor to the heatmap value, and then cast the value to an integer. The value
of the multiplier influences the *variation degree*.

 - If the value is large, then two close tiles are likely to have a different
   variation seed and therefore a different variation tile.
 - It the value is low, a lot of neighbor tiles will have the same variation
   seed and therefore will show the same tile.
