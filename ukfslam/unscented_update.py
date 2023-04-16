from sqrt_posdef import sqrt_posdef
import numpy as np


def unscented_update(zfunc, dzfunc, x, P, z, R, *args):
    """
    x,P = unscented_update(zfunc,dzfunc, x,P, z,R, ...)

    Algorithm implemented as described in: 
    Simon Julier's PhD thesis pp 20--23.

    INPUTS:
    zfunc - observe model.
    dzfunc - observation residual: v = mydfunc(z, z_predict);
    x, P - predict mean and covariance
    z, R - observation and covariance (observation noise is assumed additive)
    ... - optional arguments such that 'zfunc' has the form: z = myfunc(x, ...)

    OUTPUTS:
    x, P - updated mean and covariance

    NOTES:
    1. This function uses the unscented transform to compute a Kalman update.

    2. The function 'zfunc' is the non-linear observation function. This function may be passed 
    any number of additional parameters.
        eg, z = my_observe_model(x, p1, p2);

    3. The residual function 'dzfunc' is required to deal with discontinuous functions. Some non-linear 
    functions are discontinuous, but their residuals are not equal to the discontinuity. A classic
    example is a normalised angle measurement model:
        z1 = angle_observe_model(x1, p1, p2, p3);   # lets say z1 == pi
        z2 = angle_observe_model(x2, p1, p2, p3);   # lets say z2 == -pi
        dz = z1 - z2;                               # dz == 2*pi -- this is wrong (must be within +/- pi)
        dz = residual_model(z1, z2);                # dz == 0 -- this is correct
    Thus, 'residual_model' is a function that computes the true residual of z1-z2. If the function 
    'zfunc' is not discontinuous, or has a trivial residual, just pass None to parameter 'dzfunc'.

    4. The functions 'zfunc' and 'dzfunc' must be vectorised. That is, they must be able to accept a set of 
    states as input and return a corresponding set of results. So, for 'zfunc', the state x will not be a 
    single column vector, but a matrix of N column vectors. Similarly, for 'dzfunc', the parameters z and 
    z_predict will be equal-sized matrices of N column vectors.

    EXAMPLE USE:
    x,P = unscented_update(angle_observe_model, residual_model, x,P, z,R, a, b, c);
    x,P = unscented_update(range_model, None, x,P, z,R);
    """
    
    # Set up some values
    D = len(x)  # state dimension
    N = D*2 + 1  # number of samples
    scale = 3  # want scale = D+kappa == 3
    kappa = scale-D

    # Create samples
    Ps = sqrt_posdef(P) * sqrt(scale)
    ss = np.concatenate((np.concatenate((x, repvec(x,D) + Ps), axis=1), repvec(x,D) - Ps), axis=1)


def default_dfunc(y1, y2):
    e = y1 - y2
    return e

def repvec(x, N):
    a = np.copy(x)
    x = np.copy(x)
    for i in range(N-1):
        x = np.hstack((np.copy(x),a))
    return x 
