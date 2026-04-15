import numpy as np

def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    if((len(set_a) + len(set_b)) == 0):
        return 0
    intersect = np.intersect1d(set_a,set_b)
    union = np.union1d(set_a,set_b)
    return len(intersect) / len(union)