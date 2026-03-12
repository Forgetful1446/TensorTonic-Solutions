def precision_recall_at_k(recommended, relevant, k):
    relevant = set(relevant)

    top_k = set(recommended[:k])
    hits = len(top_k & relevant)

    precision = hits / k
    recall = hits / len(relevant)

    return [precision, recall]