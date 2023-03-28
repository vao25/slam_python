from pi_to_pi import pi_to_pi
from compute_jacobians import compute_jacobians
from KF_cholesky_update import KF_cholesky_update

def feature_update(particle, z, idf, R):
    # particle= feature_update(particle, z, idf, R)
    # Having selected a new pose from the proposal distribution, this pose is assumed
    # perfect and each feature update may be computed independently and without pose uncertainty.
    
    xf = particle.xf[:,idf]
    Pf = particle.Pf[:,:,idf]
    
    zp, Hv, Hf, Sf = compute_jacobians(particle, idf, R)
    v = z - zp
    v[1,:] = pi_to_pi(v[1,:])
    
    for i in range(len(idf)):
        vi = v[:,i]
        Hfi = Hf[:,:,i]
        Pfi = Pf[:,:,i]
        xfi = xf[:,i]
        
        xf[:,i], Pf[:,:,i] = KF_cholesky_update(xfi, Pfi, vi, R, Hfi)
        
    particle.xf[:,idf] = xf
    particle.Pf[:,:,idf] = Pf
    
    return particle 
