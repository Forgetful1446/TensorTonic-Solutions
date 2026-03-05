import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if(max_len is None):
        max_len = 0
        for i in range(len(seqs)):
            max_len = max(max_len, len(seqs[i]))
    
    padded = [[pad_value for i in range(max_len)] for i in range(len(seqs))]

    for i in range(len(seqs)):
        for j in range(min(len(seqs[i]), len(padded[i]))):
            padded[i][j] = seqs[i][j]

    return padded

print(pad_sequences([[1,2,3],[4]], -1, None))