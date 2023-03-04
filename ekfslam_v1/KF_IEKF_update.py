import numpy as np

def KF_IEKF_update(x,P, z,R, hfun,hjac, N):
"""
[x,P] = KF_IEKF_update(x,P, z,R, hfun,hjac, N)

 INPUTS:
   x - x(k|k-1) - predicted state
   P - P(k|k-1) - predicted covariance
   z - observation
   R - observation uncertainty
   hfun - function for computing the innovation, given the non-linear observation model: v = hfun(x,z);
   hjac - function for computing the observation model jacobian: H = hjac(x);
   N - number of iterations of the IEKF update

 OUTPUTS:
   x - x(k|k) - a posteri state
   P - P(k|k) - a posteri covariance

 Uses iterated EKF (cite Bar-Shalom 01 - p406). This implementation is rather inefficient for 
 SLAM, as it involves the inversion of P (ie, the update is O(n^3) for n landmarks.
"""
    
    xo= x # prior values
    Po= P
    Poi= np.linalg.inv(P)
    Ri= np.linalg.inv(R)

    for i in range(N): # iterate solution
        H= hjac(x)
        P= calculate_P(Po,H,R)

        v= hfun(x,z) # to cope with discontinuous models, need this form rather than: v= z - feval(hfun,x); 
        x= calculate_x(v,x,P,xo,Poi,H,Ri)    
    H= hjac(x) # final iteration 
    P= calculate_P(Po,H,R)
    return x,P

def calculate_P(P,H,R):
    HP= np.dot(H,P)
    PHt= np.dot(P,H.T)
    S= np.dot(H,PHt) + R
    P= P - np.dot(np.dot(PHt, np.linalg.inv(S)), HP)
    P= make_symmetric(P) # for assurance
    return P

def calculate_x(v,x,P,xo,Poi,H,Ri):
    M1= np.dot(P, np.dot(H.T, Ri))
    M2= np.dot(P, np.dot(Poi, (x-xo)))
    x= x + np.dot(M1,v) - M2
    return x

def make_symmetric(P):
    P= (P+P.T)/2
    return P
