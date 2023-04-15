import numpy as np

def sqrt_posdef(P):
    # R = sqrt_posdef(P, type)
    # INPUTS: P - symmetric positive definite matrix
    # OUTPUT: R - square-root of P, such that P = R*R'
    # Compute the square-root of a symmetric positive definite matrix.
    
    # cholesky decomposition (triangular), P = R*R'
    R = np.transpose(np.linalg.cholesky(P))
    return R 
