import random as rd
from rolepy.generate import Chunk
from rolepy.globals import Ordinal


def merge_dict(dict_a, dict_b):
    merger = {key: value for key, value in dict_a.items()}
    for key, value in dict_b.items():
        merger[key] = value
    return merger


def custom_hash(seeds):
    root_seed = 0
    for seed in seeds:
        rd.seed(root_seed + seed)
        root_seed = rd.randint(0, 2**32 - 1)
    return root_seed


class Heatmap:

    def __init__(self, seed):
        self.seed = seed
        self.chunks = dict()

    def __getitem__(self, position):
        x, y = position
        h = 2 ** Chunk.SIZE + 1
        chunk = self.generate_chunk(y // h, x // h)
        return chunk[y % h][x % h]

    def set_chunk_seed(self, i, j):
        chunk_seed = custom_hash([self.seed, i, j])
        rd.seed(chunk_seed)

    def generate_chunk(self, i, j):
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
