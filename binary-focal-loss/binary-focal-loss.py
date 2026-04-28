import numpy as np

def binary_focal_loss(predictions, targets, alpha, gamma):
    """
    Compute the mean binary focal loss.
    
    predictions: list/array of probabilities (0 < p < 1)
    targets: list/array of binary labels (0 or 1)
    alpha: balancing factor
    gamma: focusing parameter
    
    return: mean focal loss
    """
    
    predictions = np.array(predictions, dtype=float)
    targets = np.array(targets, dtype=int)
    
    # Compute p_t
    p_t = np.where(targets == 1, predictions, 1 - predictions)
    
    # Compute focal loss for each sample
    loss = -alpha * ((1 - p_t) ** gamma) * np.log(p_t)
    
    # Return mean loss
    return float(np.mean(loss))