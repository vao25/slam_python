import numpy as np
import configfile as c # ** USE THIS FILE TO CONFIGURE THE EKF-SLAM **
from compute_steering import compute_steering
from vehicle_model import vehicle_model
from add_control_noise import add_control_noise
from predict import predict
from observe_heading import observe_heading
from get_observations import get_observations
from add_observation_noise import add_observation_noise
from data_associate_known import data_associate_known
from data_associate import data_associate
from update import update
from augment import augment

def ekfslam_sim(lm, wp):
"""
 data= ekfslam_sim(lm, wp)

 INPUTS: 
   lm - set of landmarks
   wp - set of waypoints

 OUTPUTS:
   data - a data structure containing:
       data.true: the vehicle 'true'-path (ie, where the vehicle *actually* went)
       data.path: the vehicle path estimate (ie, where SLAM estimates the vehicle went)
       data.state(k).x: the SLAM state vector at time k
       data.state(k).P: the diagonals of the SLAM covariance matrix at time k

 NOTES:
   This program is a SLAM simulator. To use, create a set of landmarks and 
   vehicle waypoints (ie, waypoints for the desired vehicle path).
       The configuration of the simulator is managed by the script file
   'configfile.py'. To alter the parameters of the vehicle, sensors, etc
   adjust this file. There are also several switches that control certain
   filter options.
 
 Version 1.0
"""

    # initialise states
    xtrue = np.zeros((3,1))
    x = np.zeros((3,1))
    P = np.zeros((3,3))   

    # initialise other variables and constants
    dt = c.DT_CONTROLS
    dtsum = 0
    ftag = np.arange(lm.shape[1])
    da_table = np.zeros((1, lm.shape[1]))
    iwp = 1
    G = 0
    data = initialise_store(x,P,x)
    QE = c.Q
    RE = c.R
    if c.SWITCH_INFLATE_NOISE:
        QE = 2*c.Q
        RE = 8*c.R
    if c.SWITCH_SEED_RANDOM:
        np.random.seed(c.SWITCH_SEED_RANDOM)
        
    
