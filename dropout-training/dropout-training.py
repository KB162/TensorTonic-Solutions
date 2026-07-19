import numpy as np 
def dropout(x , p=0.5 ,rng=None):
    x =np.asarray(x , dtype=float)
    #rng stands for random number generator 
    rng = rng if isinstance(rng , np.random.Generator) else np.random.default_rng(0)
    keep = 1.0 - p
    mask = (rng.random(x.shape) < keep).astype(float) / keep
    return x * mask , mask