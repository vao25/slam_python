import numpy as np
import json
from ukfslam_sim import ukfslam_sim

with open('file.json', 'r') as fr:
    env = json.load(fr)

lm = np.array([[],[]])
for i in range(len(env["lm"])):
    lm = np.append(lm, [[env["lm"][i][0]], [env["lm"][i][1]]], axis = 1)
    
wp = np.array([[],[]])
for i in range(len(env["wp"])):
    wp = np.append(wp, [[env["wp"][i][0]], [env["wp"][i][1]]], axis = 1)
    
data = ukfslam_sim(lm, wp, env["x3"])

print("Finished!")
