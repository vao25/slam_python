import numpy as np
from stratified_resample import stratified_resample

def resample_particles(particles, Nmin, doresample):
    # particles= resample_particles(particles, Nmin, doresample)
    # Resample particles if their weight variance is such that N-effective is less than Nmin.
    
    N = len(particles)
    w = np.zeros(N)
    for i in range(N):
        w[i] = particles[i].w
    ws = sum(w)
    w = w/ws
    for i in range(N):
        particles[i].w = particles[i].w / ws
    
    keep, Neff = stratified_resample(w)
    if Neff < Nmin and doresample == 1:
        particles = particles[keep]
        for i in range(N):
            particles[i].w = 1/N
    return particles
