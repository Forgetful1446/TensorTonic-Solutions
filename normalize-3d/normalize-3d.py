import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    def norm(v):
        return np.sqrt(sum(x*x for x in v))
    
    def normalize_one(vec):
        n = norm(vec)
        if n == 0:
            return tuple(0 for _ in vec)
        return tuple(x / n for x in vec)

    if isinstance(v[0], (int, float)):
        return np.array(normalize_one(v))

    elif isinstance(v[0], (list, tuple)):
        return np.array([normalize_one(vec) for vec in v])