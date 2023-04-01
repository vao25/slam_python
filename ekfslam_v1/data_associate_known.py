import numpy as np

def data_associate_known(x, z, idz, table):
    # [zf,idf,zn, table]= data_associate_known(x,z,idz, table)
    # For simulations with known data-associations, this function maintains a feature/observation lookup table. It returns the updated table, the set of associated observations and the set of observations to new features.
    
    zf = np.array([])
    idf = np.array([])
    zn = np.array([])
    idn = np.array([])
    
    # find associations (zf) and new features (zn)
    for i in range(len(idz)):
        ii = idz[i]
        if table[0,ii] == -1: # new feature
            np.append(zn, z[:,i], axis = 1)
            np.append(idn, ii, axis = 1)
        else:
            np.append(zf, z[:,i], axis = 1)
            np.append(idf, table[0,ii], axis = 1)
    
    # add new feature IDs to lookup table        
    Nxv = 3 # number of vehicle pose states
    Nf = (len(x) - Nxv)/2 # number of features already in map
    table[0,idn] = Nf + (1:zn.shape[1]) # add new feature positions to lookup table
    return zf, idf, zn, table

