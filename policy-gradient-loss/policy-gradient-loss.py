def policy_gradient_loss(log_probs, rewards, gamma):
    """
    Compute REINFORCE policy gradient loss with mean-return baseline.
    """
    n = len(rewards)

    returns = [0.0] * n
    returns[-1] = rewards[-1]
    
    for i in range(n - 2, -1, -1):
        returns[i] = rewards[i] + gamma * returns[i + 1]
    
    baseline = sum(returns) / n

    loss = 0.0
    for i in range(n):
        advantage = returns[i] - baseline
        loss += log_probs[i] * advantage
    
    return -loss / n