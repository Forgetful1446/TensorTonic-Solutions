def weighted_moving_average(values, weights):
    """
    Compute the weighted moving average using the given weights.
    """
    n = len(values)
    k = len(weights)
    w_sum = sum(weights)
    
    result = []
    
    for i in range(n - k + 1):
        s = 0.0
        for j in range(k):
            s += weights[j] * values[i + j]
        result.append(s / w_sum)
    
    return result