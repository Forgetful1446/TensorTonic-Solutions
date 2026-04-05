import numpy as np

def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    X = np.array(X)
    A = np.dot(X.T, X) + np.dot(lam, np.eye(X.shape[1]))
    A = np.linalg.inv(A)
    B = np.dot(X.T, y)
    return np.dot(A,B)