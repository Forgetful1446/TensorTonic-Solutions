import numpy as np

def mean_squared_error(y_pred, y_true):
    if(len(y_pred) != len(y_true)): return -1
    mse = 0
    for i in range(len(y_pred)):
        mse += (y_true[i] - y_pred[i]) ** 2
    return mse / len(y_pred)