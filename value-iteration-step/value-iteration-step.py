def value_iteration_step(values, transitions, rewards, gamma):
    n = len(values)
    new_values = [0.0] * n

    for s in range(n):
        best = float("-inf")

        for a in range(len(rewards[s])):
            q = rewards[s][a]

            # expected future value
            for sp in range(n):
                q += gamma * transitions[s][a][sp] * values[sp]

            best = max(best, q)

        new_values[s] = best

    return new_values