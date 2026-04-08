import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    w = np.array(w)
    g = np.array(g)
    G = np.array(G)
    
    Gt = G + g * g
    wt = w - (lr / (np.sqrt(Gt + eps))) * g
    
    return (wt, Gt)