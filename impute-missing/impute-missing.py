import numpy as np

def impute_missing(X, strategy='mean'):
    X = np.array(X, dtype=float)
    original_shape = X.shape
    
    if X.ndim == 1:
        X = X.reshape(-1, 1)

    if strategy == 'mean':
        values = np.nanmean(X, axis=0)
    elif strategy == 'median':
        values = np.nanmedian(X, axis=0)
    else:
        raise ValueError("strategy must be 'mean' or 'median'")

    values = np.where(np.isnan(values), 0, values)

    inds = np.where(np.isnan(X))

    X[inds] = np.take(values, inds[1])
    
    if len(original_shape) == 1:
        return X.flatten()

    return X