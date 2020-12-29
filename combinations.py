import numpy as np


def combinations(*items):
    """Return number of possible permutations of items in each group"""
    return np.prod([i for i in items if i != 0])
