def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    candidates = []
    for i, s in enumerate(scores):
        if i in rated_indices:
            continue
        candidates.append((s, i))

    candidates.sort(key=lambda x: (-x[0], x[1]))


    result = [i for _, i in candidates[:k]]

    return result