
import numpy as np
import graph_tool as gt
from scipy.stats import sem as scipy_sem

from comp.functions import get_2neuron_p, eval_connectivity


def get_2neuron_counts_rel_random(gpath_base):

    cp = np.zeros(5)
    ps = np.zeros((5,3))

    for gid in range(5):
        gpath = gpath_base+'-{:02d}.gt'.format(gid)
        g = gt.load_graph(gpath)
        cp[gid] += eval_connectivity(g)
        ps[gid,:] += get_2neuron_p(g)


    # # print "Unconnected: ", (1-p)**2
    # # print "Single:      ", 2*p*(1-p)
    # # print "Recip:       ", p**2

    rl_uc = ps[:,0]/((1-cp)**2)
    rl_sp = ps[:,1]/(2*cp*(1-cp))
    rl_rc = ps[:,2]/(cp**2)

    y = [np.mean(rl_uc), np.mean(rl_sp), np.mean(rl_rc)]
    y_err = [scipy_sem(rl_uc), scipy_sem(rl_sp), scipy_sem(rl_rc)]

    return np.array(y), np.array(y_err)
