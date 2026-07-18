import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A) 
    trans = [[0 for _ in range(len(A))]   #this is used to initialise [[0,0,0] , [0,0,0]] 
               for _ in range(len(A[0]))]
     
    for i in range(len(A)): 
        for j in range(len(A[0])):
            trans[j][i] = A[i][j]
    return np.array(trans)         
    pass
