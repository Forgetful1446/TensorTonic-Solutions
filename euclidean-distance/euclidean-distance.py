import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    if len(x) != len(y):
        raise ValueError

    total = 0
    for i in range(len(x)):
        total += (y[i] - x[i]) ** 2

    return np.sqrt(total)