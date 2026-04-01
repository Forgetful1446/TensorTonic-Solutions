import math

def ndcg(relevance_scores, k):
    DCG = 0
    IDCG = 0
    k = min(k, len(relevance_scores))
    for i in range(k):
        rel = relevance_scores[i]
        DCG += (2**rel - 1) / math.log2(i + 2)

    max_rel = sorted(relevance_scores, reverse=True)

    for i in range(k):
        rel = max_rel[i]
        IDCG += (2**rel - 1) / math.log2(i + 2)

    if IDCG == 0:
        return 0

    return DCG / IDCG

print(ndcg([3,1] , 5))