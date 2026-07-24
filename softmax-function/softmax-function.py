import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.asarray(x , dtype =float) #convert it to array 
    if x.ndim == 1:#if dimension is one 
        shifted = x - np.max(x)# subtract max value to make it like 
        exps = np.exp(shifted)#calculate the exponential value 
        return np.round(exps / np.sum(exps),4).tolist() # exponent / sum of the exponent values 
    elif x.ndim == 2 :#if dimension is 2d
        shifted = x - np.max(x)#calculate the shifted value 
        exps = np.exp(shifted)#calculate the exponentaial value 
        result = exps / np.sum(exps, axis =1 , keepdims=True)#
        return np.round(result,4).tolist()
    pass