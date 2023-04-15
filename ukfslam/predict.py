from scipy.linalg import block_diag
import numpy as np
from unscented_transform import unscented_transform

def predict(v, g, Q, WB, dt):
    global XX, PX
    XX = np.vstack(XX, np.array([[v], [g]]))
    PX = block_diag(PX, Q)
    XX, PX = unscented_transform(vehiclemod, vehiclediff, XX, PX, WB, dt)

def vehiclemod(x, WB, dt):
    V = x[-2,:]
    G = x[-1,:]
    x = x[:-2,:]
    x[:3,:] = vehicle_model(x, V, G, WB, dt)
    return x

def vehiclediff(x1, x2):
    dx = x1 - x2
    dx[2,:] = pi_to_pi(dx[2,:])
    return dx 
