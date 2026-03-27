import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    try:
        matrix = np.array(matrix, dtype=float)
    except:
        return None

    if matrix.ndim != 2:
        return None

    # ✅ FIX quan trọng
    if axis not in (None, 0, 1):
        return None

    if axis is None:
        if norm_type == 'l1':
            norm = np.sum(np.abs(matrix))
        elif norm_type == 'l2':
            norm = np.sqrt(np.sum(matrix**2))
        elif norm_type == 'max':
            norm = np.max(np.abs(matrix))
        else:
            return None

        if norm == 0:
            return matrix

        return matrix / norm

    if axis == 0:
        matrix = matrix.T

    result = []

    for row in matrix:
        if norm_type == 'l1':
            norm = np.sum(np.abs(row))
        elif norm_type == 'l2':
            norm = np.sqrt(np.sum(row**2))
        elif norm_type == 'max':
            norm = np.max(np.abs(row))
        else:
            return None
        
        result.append(norm)

    result = np.array(result)
    result[result == 0] = 1
    result = result.reshape(-1, 1)

    matrix = matrix / result

    if axis == 0:
        matrix = matrix.T

    return matrix