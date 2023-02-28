import numpy as np
from pi_to_pi import pi_to_pi

def vehicle_model(xv, V, G, WB, dt):
"""
 INPUTS:
   xv - vehicle pose [x;y;phi]
   V - velocity
   G - steer angle (gamma)
   WB - wheelbase
   dt - change in time

 OUTPUTS:
   xv - new vehicle pose

"""
    xv = np.array([xv[0] + V*dt*np.cos(G+xv[2]), 
                   xv[1] + V*dt*np.sin(G+xv[2]),
                   pi_to_pi(xv[2] + V*dt*np.sin(G)/WB)])
    return xv
