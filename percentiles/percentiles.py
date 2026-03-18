import numpy as np

def percentiles(x, q):
    x = np.sort(np.array(x))
    q = np.array(q)

    n = len(x)
    k = (n - 1) * (q / 100)

    floor = np.floor(k).astype(int)
    ceil = np.ceil(k).astype(int)

    delta = k - floor

    result = x[floor] + delta * (x[ceil] - x[floor])

    return result