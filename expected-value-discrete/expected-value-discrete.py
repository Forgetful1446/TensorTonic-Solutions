import numpy as np

def expected_value_discrete(x, p):
    x = np.array(x)
    p = np.array(p)

    if len(x) != len(p):
        raise ValueError("x and p must have same length")

    if np.any(p < 0):
        raise ValueError("probabilities must be non-negative")

    if not np.isclose(np.sum(p), 1):
        raise ValueError("probabilities must sum to 1")

    return np.sum(x * p)