import numpy as np

def expected_calibration_error(y_true, y_pred, n_bins):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    
    bin_indices = np.minimum((y_pred * n_bins).astype(int), n_bins - 1)
    
    ece = 0.0
    N = len(y_true)
    
    for b in range(n_bins):
        mask = bin_indices == b
        
        if np.sum(mask) == 0:
            continue
        
        acc = np.mean(y_true[mask])
        conf = np.mean(y_pred[mask])
        
        ece += (np.sum(mask) / N) * abs(acc - conf)
    
    return ece