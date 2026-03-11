import numpy as np

def entropy_node(y):
    if len(y) == 0:
        return 0.0

    y = np.asarray(y)

    _, counts = np.unique(y, return_counts=True)
    probs = counts / counts.sum()

    probs = probs[probs > 0]

    entropy = -np.sum(probs * np.log2(probs))

    return float(entropy)