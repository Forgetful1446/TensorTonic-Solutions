def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    ranking = [0 for _ in range(len(items))]

    for i in range(len(items)):
        item_rate = items[i][0]
        vote_count = items[i][1]
        ranking[i] = (vote_count/(vote_count + min_votes)) * item_rate + ((min_votes)/(vote_count + min_votes)) * global_mean
    return ranking