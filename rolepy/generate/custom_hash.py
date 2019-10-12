import random as rd


def custom_hash(seeds):
    root_seed = 0
    for seed in seeds:
        rd.seed(root_seed + seed)
        root_seed = rd.randint(0, 2**32 - 1)
    return root_seed
