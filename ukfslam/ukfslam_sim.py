def initialise_store(x, P, xtrue):
    # offline storage initialisation
    data = {}
    data['i'] = 1
    data['path'] = np.zeros((3, 1))
    data['path'][0,0] = x[0][0]
    data['path'][1,0] = x[1][0]
    data['path'][2,0] = x[2][0]
    data['true'] = np.zeros((3, 1))
    data['true'][0,0] = xtrue[0][0]
    data['true'][1,0] = xtrue[1][0]
    data['true'][2,0] = xtrue[2][0]
    data['state'] = [{}]
    data['state'][0]['x'] = np.copy(x)
    data['state'][0]['PV'] = np.copy(P)
    data['state'][0]['P'] = np.diag(np.copy(P))
    return data 

def store_data(data, x, P, xtrue):    
    # add current data to offline storage
    CHUNK = 5000
    if data['i'] == data['path'].shape[1]: # grow array in chunks to amortise reallocation
        data['path'] = np.hstack((data['path'], np.zeros((3, CHUNK))))
        data['true'] = np.hstack((data['true'], np.zeros((3, CHUNK))))
    i = data['i'] + 1
    data['i'] = i
    data['path'][0,i-1] = x[0][0]
    data['path'][1,i-1] = x[1][0]
    data['path'][2,i-1] = x[2][0]
    data['true'][0,i-1] = xtrue[0][0]
    data['true'][1,i-1] = xtrue[1][0]
    data['true'][2,i-1] = xtrue[2][0]
    data['state'].append({})
    data['state'][i-1]['x'] = np.copy(x)
    #data['state'][i-1]['P'] = P
    data['state'][i-1]['P'] = np.diag(P)
    data['state'][i-1]['PV'] = np.copy(P[0:3,0:3])
    return data

def finalise_data(data):
    # offline storage finalisation
    data['path'] = data['path'][:, 0:data['i']]
    data['true'] = data['true'][:, 0:data['i']]
    return data
