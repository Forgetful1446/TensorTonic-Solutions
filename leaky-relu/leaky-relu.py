import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    x = np.array(x)  # đảm bảo output luôn là NumPy array
    return np.where(x >= 0, x, alpha * x)