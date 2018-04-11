
import numpy as np
import graph_tool as gt
from scipy.stats import sem as scipy_sem

from comp.functions import get_2neuron_p, eval_connectivity


def get_2neuron_counts_rel_random(gpath_base):

    n_graphs = 5

    cp = np.zeros(n_graphs)
    ps = np.zeros((n_graphs,3))

    for gid in range(n_graphs):
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


def get_2neuron_counts_rel_rew(gpath_base, rew_gpath_base):

    n_graphs = 5

    ps_org = np.zeros((n_graphs,3))
    ps_rew = np.zeros((n_graphs,3))

    for gid in range(n_graphs):
        gpath = gpath_base+'-{:02d}.gt'.format(gid)
        g = gt.load_graph(gpath)
        ps_org[gid,:] += get_2neuron_p(g)

        hpath = rew_gpath_base+'-{:02d}.gt'.format(gid)
        h = gt.load_graph(hpath)
        ps_rew[gid,:] += get_2neuron_p(h)

    rl_uc = ps_org[:,0]/ps_rew[:,0]
    rl_sp = ps_org[:,1]/ps_rew[:,1]
    rl_rc = ps_org[:,2]/ps_rew[:,2]

    y = [np.mean(rl_uc), np.mean(rl_sp), np.mean(rl_rc)]
    y_err = [scipy_sem(rl_uc), scipy_sem(rl_sp), scipy_sem(rl_rc)]

    return np.array(y), np.array(y_err)
