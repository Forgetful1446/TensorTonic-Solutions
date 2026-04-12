import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    g = np.array(g)
    
    if max_norm <= 0:
        return g
    
    L2_norm = np.sqrt(np.sum(g ** 2))
    
    if L2_norm > max_norm:
        g = g * (max_norm / L2_norm)
    return g
