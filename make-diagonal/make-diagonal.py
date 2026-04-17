import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    diagonal_matrix = [[0 for _ in range(len(v))] for _ in range(len(v))]
    
    for i in range(len(v)):
        diagonal_matrix[i][i] = v[i]
    return np.array(diagonal_matrix)