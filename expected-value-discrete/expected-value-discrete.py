import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.asarray(x, dtype = float)
    p = np.asarray(p, dtype = float)
    if x.shape != p.shape:
        raise ValueError("x and p must be in the same shape")
    if abs(p.sum() - 1.0) > 1e-6:   
        raise ValueError("probablities must have sum to 1")
    expected_value =  float(np.sum(x * p))
    return expected_value
    pass
