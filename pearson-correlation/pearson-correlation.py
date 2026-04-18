import numpy as np

def pearson_correlation(X):
    """
    Compute Pearson correlation matrix from dataset X.
    """
    X = np.array(X)

    if X.ndim != 2 or X.shape[0] < 2:
        return None

    mean = np.mean(X, axis=0)
    X_centered = X - mean

    cov = (X_centered.T @ X_centered) / (X.shape[0] - 1)

    std = np.sqrt(np.diag(cov))

    denom = np.outer(std, std)

    with np.errstate(divide='ignore', invalid='ignore'):
        corr = cov / denom

    return corr