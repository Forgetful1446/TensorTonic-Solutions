def binning(values, num_bins):
	"""
	Assign each value to an equal-width bin.
	"""
	max_val = max(values)
	min_val = min(values)
	range_bin  =  max_val - min_val
	width = range_bin / num_bins
	binned  = [0 for _ in range(len(values))]
	if width == 0:
		return binned
	for i in range(len(values)):
		bin_idx = int ((values[i] - min_val) / width)
		binned[i] =  bin_idx
		if values[i] == max_val:
			binned[i] -= 1
	return binned