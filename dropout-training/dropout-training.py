import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """

    x = np.array(x, dtype=float)

    keep_prob = 1 - p

    # chọn random generator
    if rng is None:
        rand = np.random.random(x.shape)
    else:
        rand = rng.random(x.shape)

    mask = (rand < keep_prob) / keep_prob

    x_drop = x * mask

    return x_drop, mask