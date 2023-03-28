import numpy as np

def add_feature(particle, z, R):
    # add new features 
    lenz = z.shape[1]
    xf = np.zeros((2,lenz))
    Pf = np.zeros((2,2,lenz))
    xv = particle.xv
    
    for i in range(lenz):
        r = z[0,i]
        b = z[1,i]
        s = np.sin(xv[2] + b)
        c = np.cos(xv[2] + b)
        
        xf[:,i] = [xv[0] + r*c, xv[1] + r*s]
        
        Gz = np.array([[c, -r*s], [s,  r*c]])
        Pf[:,:,i] = np.dot(np.dot(Gz, R), Gz.T)
        
    lenx = particle.xf.shape[1]
    ii = np.arange(lenz) + (lenx)
    particle.xf[:,ii] = xf
    particle.Pf[:,:,ii] = Pf
    return particle
