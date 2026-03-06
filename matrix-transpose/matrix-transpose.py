import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    B = [[0 for _ in range(len(A))]for _ in range(len(A[0]))]
    
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[j][i] = A[i][j]

    return np.array(B)