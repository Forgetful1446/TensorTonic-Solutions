def binning(values, num_bins):
    max_val = max(values)
    min_val = min(values)
    
    range_bin = max_val - min_val
    width = range_bin / num_bins
    
    binned = [0] * len(values)
    
    if width == 0:
        return binned
    
    for i in range(len(values)):
        x = values[i]
        
        if x == max_val:
            bin_idx = num_bins - 1
        else:
            bin_idx = int((x - min_val) / width)
        
        binned[i] = bin_idx
    
    return binned