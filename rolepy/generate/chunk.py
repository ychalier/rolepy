import random as rd
from rolepy.engine.core.enums import Ordinal


class Chunk(list):
    """A fixed-size squares of [-1, 1] floats, main component of a heatmap."""

    SIZE = 6  # 2^n + 1

    def __init__(self):
        super(Chunk, self).__init__()
        size = 2 ** Chunk.SIZE + 1
        for _ in range(size):
            self.append([None for j in range(size)])

    def diamond_square(self, base=None):
        """Fill the chunk with random values according to the diamond-square
           algorithm. The `base` argument allows for constraining positions to
           definite values.
        """
        if base is None:
            base = dict()
        size = 2 ** Chunk.SIZE + 1
        for i, j in base:
            self[i][j] = base[i, j]
        for i in [0, -1]:
            for j in [0, -1]:
                if self[i][j] is None:
                    self[i][j] = rd.uniform(-1, 1)
        i = size - 1
        while i > 1:
            step = i // 2
            for pos_x in range(step, size, i):
                for pos_y in range(step, size, i):
                    if self[pos_x][pos_y] is not None:
                        continue
                    avg = .25 * (
                        self[pos_x - step][pos_y - step]
                        + self[pos_x - step][pos_y + step]
                        + self[pos_x + step][pos_y + step]
                        + self[pos_x + step][pos_y - step]
                    )
                    self[pos_x][pos_y] = avg + \
                        rd.uniform(-step / size, step / size)
            offset = 0
            for pos_x in range(0, size, step):
                if offset == 0:
                    offset = step
                else:
                    offset = 0
                for pos_y in range(offset, size, i):
                    if self[pos_x][pos_y] is not None:
                        continue
                    avg_sum = 0
                    n_neihgbors = 0.
                    if pos_x >= step:
                        avg_sum += self[pos_x - step][pos_y]
                        n_neihgbors += 1.
                    if pos_x + step < size:
                        avg_sum += self[pos_x + step][pos_y]
                        n_neihgbors += 1.
                    if pos_y >= step:
                        avg_sum += self[pos_x][pos_y - step]
                        n_neihgbors += 1.
                    if pos_y + step < size:
                        avg_sum += self[pos_x][pos_y + step]
                        n_neihgbors += 1.
                    self[pos_x][pos_y] = avg_sum / n_neihgbors + \
                        rd.uniform(-step / size, step / size)
            i = step

    def extract_border_as_base(self, border):
        """Extract a border of the chunk to be used as constraint for the
           generation of another chunk.
        """
        size = 2 ** Chunk.SIZE + 1
        if border == Ordinal.EAST:
            return {(i, 0): self[i][-1] for i in range(size)}
        if border == Ordinal.SOUTH:
            return {(-1, j): self[0][j] for j in range(size)}
        if border == Ordinal.NORTH:
            return {(0, j): self[-1][j] for j in range(size)}
        return {(i, -1): self[i][0] for i in range(size)}
