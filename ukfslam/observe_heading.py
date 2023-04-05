import numpy as np
from pi_to_pi import pi_to_pi
from KF_cholesky_update import KF_cholesky_update


def observe_heading(phi, useheading):
    # Perform state update for a given heading measurement, phi,
    # with fixed measurement noise: sigmaPhi
    global XX, PX
    
    if useheading == 0:
        return
    sigmaPhi = 1 * np.pi / 180 # radians, heading uncertainty
    
    H = np.zeros(len(XX))
    H[2] = 1
    v = pi_to_pi(phi - XX[2])
    
    XX, PX = KF_cholesky_update(XX, PX, v, sigmaPhi**2, H)
