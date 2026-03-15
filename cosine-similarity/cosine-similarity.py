import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    norm_a = 0
    norm_b = 0
    dot = 0
    for i in range(len(a)):
        norm_a += a[i] ** 2
        norm_b += b[i] ** 2
        dot += a[i] * b[i]
    if norm_a == 0 or norm_b == 0:
        return 0
    return dot/ (np.sqrt(norm_a) * np.sqrt(norm_b))