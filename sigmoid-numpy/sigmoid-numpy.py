import numpy as np

def sigmoid(x): # convert the array into numpy array then apply the sigmoid formula 
    """
    Vectorized sigmoid function.
    """
    x = np.array(x)
    return 1 / (1 + np.exp(-x)) 
    pass