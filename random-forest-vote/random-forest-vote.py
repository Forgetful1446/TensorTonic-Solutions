import numpy as np

def random_forest_vote(predictions):
    """
    Compute the majority vote from multiple tree predictions.
    """
    
    predictions = np.array(predictions).T
    result  = [0 for _ in range(len(predictions))]
    
    for i in range(len(predictions)):
        values, counts = np.unique(predictions[i], return_counts=True)
        most_frequent = values[np.argmax(counts)]
        result[i] = most_frequent
    return result