
import numpy as np
from scipy import stats


def dict_to_array(int_dict, list_length):
    '''
    takes integer defaultdict and converts to array

    Example:

       {0:21, 2:18, 3:11, 4:94}

    converted with list_length=6 returns
 
       [21, 0, 18, 11, 94, 0, 0]

    as np.array

    Important: Does NOT check or return error if 
    list_length < than largest key of int_dict with
    non-zero entr
    '''
    out_array = np.zeros(list_length)
    for i in range(list_length):
        out_array[i] = int_dict[i]
    return out_array


def process_ecounts(org_data, rew_data, max_ecount):
    '''
    takes the edge counts data structures for original and
    rewired networks and computes the relative over-
    representation of the edge counts. 

    averages over the data structure which contains data
    from 5 networks and computes the standard error of the
    mean.
    '''

    if not len(org_data) == len(rew_data):
        raise Exception("Data sets lengths not matching")

    org_array = np.zeros((len(org_data), max_ecount+1))
    rew_array = np.zeros((len(rew_data), max_ecount+1))

    for gid,ecounts in org_data.iteritems():
        org_array[int(gid),:] += dict_to_array(ecounts, max_ecount+1)
    for gid,ecounts in rew_data.iteritems():
        rew_array[int(gid),:] += dict_to_array(ecounts, max_ecount+1)

    rel_ecounts = (org_array - rew_array)/rew_array

    ecounts_mu = np.mean(rel_ecounts, axis = 0)
    ecounts_sem =  stats.sem(rel_ecounts, axis = 0, ddof = 0)
        
    return ecounts_mu, ecounts_sem
