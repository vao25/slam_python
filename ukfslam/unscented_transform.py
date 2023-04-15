from sqrt_posdef import sqrt_posdef
import numpy as np

def unscented_transform(func, dfunc, x, P, *args):
    # Set up some values
    D = len(x)  # state dimension
    N = D*2 + 1  # number of samples
    scale = 3  # want scale = D+kappa == 3
    kappa = scale-D

    # Create samples
    Ps = sqrt_posdef(P) * sqrt(scale)
    ss = np.concatenate((np.concatenate((x, repvec(x,D) + Ps), axis=1), repvec(x,D) - Ps), axis=1)

    # Transform samples according to function 'func'
    if dfunc is None:
        dfunc = default_dfunc
    ys = func(ss, *args)  # compute (possibly discontinuous) transform
    base = repvec(y[:,0],N)  # set first transformed sample as the base
    delta = dfunc(base, ys)  # compute correct residual
    ys = base - delta  # offset ys from base according to correct residual

    # Calculate predicted observation mean
    idx = np.arange(2,N+1)
    y = (2*kappa*ys[:,0] + np.sum(ys[:,idx], axis=1)) / (2*scale)

    # Calculate new unscented covariance
    dy = ys - repvec(y,N)
    Y = (2*kappa*dy[0]*np.dot(dy[:,0],np.transpose(dy[:,0])) + np.dot(dy[:,idx],np.transpose(dy[:,idx]))) / (2*scale)
    # Note: if x is a matrix of column vectors, then x*x' produces the sum of outer-products.

    return y, Y

def default_dfunc(y1, y2):
    e = y1 - y2
    return e

def repvec(x, N):
    x = x[:, np.ones((1, N))]
    return x
