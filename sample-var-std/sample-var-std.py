import numpy as np

def sample_var_std(x):
    """
    Compute sample variance and standard deviation.
    """
    mean_x = np.mean(x)
    
    var = np.sum((x - mean_x) ** 2) / (len(x) - 1)
    
    return (var, np.sqrt(var))