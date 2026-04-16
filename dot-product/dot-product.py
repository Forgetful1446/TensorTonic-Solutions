import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    if(len(x) != len(y)):
        raise ValueError()
    result = 0
    for i in range(len(x)):
        result += x[i] * y[i]
        
    return result