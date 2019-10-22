import random as rd


def custom_hash(seeds):
    """Return a custom hash value given a set of integers."""
    root_seed = 0
    for seed in seeds:
        rd.seed(root_seed + seed)
        root_seed = rd.randint(0, 2**32 - 1)
    return root_seed
