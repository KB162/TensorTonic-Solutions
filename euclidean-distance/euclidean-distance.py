import numpy as np

def euclidean_distance(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.shape != y.shape:
        raise ValueError("Vectors must have the same shape.")

    dis = 0.0

    for i in range(len(x)):
        dis += (x[i] - y[i]) ** 2

    return np.sqrt(dis)