def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    mean = 0
    var = 0
    rk =  [1.0 for _ in range(max_lag + 1)]

    for i in series:
        mean += i
    
    mean /= len(series)

    for i in series:
        var += (i - mean) * (i - mean)

    for k in range(1, max_lag + 1):
        cov = 0
        for i in range(len(series) - k):
            cov += (series[i] - mean) * (series[i + k] - mean)
        if var != 0:
            rk[k] = cov / var
        else: 
            rk[k] = 0
    
    return rk