from pi_to_pi import pi_to_pi

def predict_true(xv, V, G, WB, dt):
    xv[0] = xv[0] + V*dt*cos(G+xv[2])
    xv[1] = xv[1] + V*dt*sin(G+xv[2])
    xv[2] = pi_to_pi(xv[2] + V*dt*sin(G)/WB)
    return xv
