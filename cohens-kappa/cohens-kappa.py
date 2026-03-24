import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    agree = 0
    rateLabel = [[0,0] for _ in range(max(rater1) + 1)]

    for i in range(len(rater1)):
        if(rater1[i] == rater2[i]):
            agree += 1
        rateLabel[rater1[i]][0] += 1
        rateLabel[rater2[i]][1] += 1
            
    po = agree / len(rater1)
    pe = 0
    for i in rateLabel:
        pe += i[0]/len(rater1) * i[1]/len(rater2)
    if (pe == 1):
        return 1
    k = (po - pe) / (1 - pe)
    return k
