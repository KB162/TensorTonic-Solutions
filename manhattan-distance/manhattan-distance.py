import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    x = np.asarray(x , dtype=float) #convert the input to arrray 
    y = np.asarray(y , dtype=float)

    dis = 0.0 #initialise the distance
    for i in range(len(x)): #for evry element we subtratc the values of x and y and add them to dis
        dis += abs(x[i] - y[i])
    return dis     
    