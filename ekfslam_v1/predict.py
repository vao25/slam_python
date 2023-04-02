import numpy as np
from pi_to_pi import pi_to_pi

def predict(x, P, v, g, Q, WB, dt):    
    """
    [xn,Pn]= predict (x,P,v,g,Q,WB,dt)

     Inputs:
       x, P - SLAM state and covariance
       v, g - control inputs: velocity and gamma (steer angle)
       Q - covariance matrix for velocity and gamma
       WB - vehicle wheelbase
       dt - timestep

     Outputs: 
       xn, Pn - predicted state and covariance
    """
    
    s = np.sin(g + x[2])
    c = np.cos(g + x[2])
    vts = v * dt * s
    vtc = v * dt * c
    
    # jacobians   
    Gv = np.array([[1, 0, -vts],
                   [0, 1,  vtc],
                   [0, 0, 1]])
    Gu = np.array([[dt*c, -vts],
                   [dt*s,  vtc],
                   [dt*np.sin(g)/WB, v*dt*np.cos(g)/WB]])
  
    # predict covariance
    P[0:3, 0:3] = Gv.dot(P[0:3, 0:3]).dot(Gv.T) + Gu.dot(Q).dot(Gu.T)
    if P.shape[0] > 3:
        P[0:3, 3:] = Gv.dot(P[0:3, 3:])
        P[3:, 0:3] = P[0:3, 3:].T
    
    # predict state
    x[0:3] = [x[0] + vtc, 
              x[1] + vts,
              pi_to_pi(x[2]+ v*dt*np.sin(g)/WB)]
    
    return x, P
