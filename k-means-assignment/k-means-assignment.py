def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid based on squared Euclidean distance.
    """
    assignments = []
    
    for p in points:
        min_dist = float('inf')
        closest_centroid_idx = -1
        
        for idx, c in enumerate(centroids):
            sq_dist = 0
            for d in range(len(p)):
                sq_dist += (p[d] - c[d]) ** 2
        
            if sq_dist < min_dist:
                min_dist = sq_dist
                closest_centroid_idx = idx
                
        assignments.append(closest_centroid_idx)
        
    return assignments