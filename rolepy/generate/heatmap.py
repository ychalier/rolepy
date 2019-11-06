import random as rd
from rolepy.generate import Chunk
from rolepy.generate import custom_hash
from rolepy.engine.core.enums import Ordinal


def merge_dict(dict_a, dict_b):
    """Merge the content of two dictionnaries into one."""
    merger = dict_a.copy()
    for key, value in dict_b.items():
        merger[key] = value
    return merger


class Heatmap:
    """A 2D infinite grid of [-1, 1] coherent random values."""

    def __init__(self, seed):
        self.seed = seed
        self.chunks = dict()

    def __getitem__(self, position):
        pos_x, pos_y = position
        size = 2 ** Chunk.SIZE + 1
        chunk = self.generate_chunk(pos_y // size, pos_x // size)
        return chunk[pos_y % size][pos_x % size]

    def set_chunk_seed(self, i, j):
        """Set the random seed before the generation of a chunk."""
        chunk_seed = custom_hash([self.seed, i, j])
        rd.seed(chunk_seed)

    def generate_chunk(self, i, j):
        """Return the chunk at coordinates (i, j), and generate it if needed."""
        if (i, j) in self.chunks:
            return self.chunks[i, j]
        base = dict()
        if i > 0:
            base = merge_dict(base, self.generate_chunk(
                i - 1, j).extract_border_as_base(Ordinal.NORTH))
        if i < 0:
            base = merge_dict(base, self.generate_chunk(
                i + 1, j).extract_border_as_base(Ordinal.SOUTH))
        if j > 0:
            base = merge_dict(base, self.generate_chunk(
                i, j - 1).extract_border_as_base(Ordinal.EAST))
        if j < 0:
            base = merge_dict(base, self.generate_chunk(
                i, j + 1).extract_border_as_base(Ordinal.WEST))
        self.set_chunk_seed(i, j)
        chunk = Chunk()
        chunk.diamond_square(base)
        self.chunks[i, j] = chunk
        return chunk
