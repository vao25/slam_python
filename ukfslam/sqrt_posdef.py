import numpy as np

def sqrt_posdef(P):
    # cholesky decomposition (triangular), P = R*R'
    R = np.transpose(np.linalg.cholesky(P))
    return R 
