import random as rd
from rolepy.globals import Ordinal


class Chunk(list):

    SIZE = 6  # 2^n + 1

    def __init__(self):
        super(Chunk, self).__init__()
        h = 2 ** Chunk.SIZE + 1
        for i in range(h):
            self.append([None for j in range(h)])

    def diamond_square(self, base=dict()):
        h = 2 ** Chunk.SIZE + 1
        for i, j in base:
            self[i][j] = base[i, j]
        for i in [0, -1]:
            for j in [0, -1]:
                if self[i][j] is None:
                    self[i][j] = rd.uniform(-1, 1)
        i = h - 1
        while i > 1:
            step = i // 2
            for x in range(step, h, i):
                for y in range(step, h, i):
                    if self[x][y] is not None:
                        continue
                    avg = .25 * (
                        self[x - step][y - step]
                        + self[x - step][y + step]
                        + self[x + step][y + step]
                        + self[x + step][y - step]
                    )
                    self[x][y] = avg + rd.uniform(-step / h, step / h)
            offset = 0
            for x in range(0, h, step):
                if offset == 0:
                    offset = step
                else:
                    offset = 0
                for y in range(offset, h, i):
                    if self[x][y] is not None:
                        continue
                    avg_sum = 0
                    n = 0.
                    if x >= step:
                        avg_sum += self[x - step][y]
                        n += 1.
                    if x + step < h:
                        avg_sum += self[x + step][y]
                        n += 1.
                    if y >= step:
                        avg_sum += self[x][y - step]
                        n += 1.
                    if y + step < h:
                        avg_sum += self[x][y + step]
                        n += 1.
                    self[x][y] = avg_sum / n + rd.uniform(-step / h, step / h)
            i = step

    def extract_border_as_base(self, border):
        h = 2 ** Chunk.SIZE + 1
        if border == Ordinal.EAST:
            return {(i, 0): self[i][-1] for i in range(h)}
        elif border == Ordinal.SOUTH:
            return {(-1, j): self[0][j] for j in range(h)}
        elif border == Ordinal.NORTH:
            return {(0, j): self[-1][j] for j in range(h)}
        elif border == Ordinal.WEST:
            return {(i, -1): self[i][0] for i in range(h)}
