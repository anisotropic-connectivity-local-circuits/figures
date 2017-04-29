
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import numpy as np
import graph_tool as gt

import sys
sys.path.append("..")
from comp.functions import get_dists_of_connected_pairs

import pickle, scipy.stats

def cnct_dst_frq(g,nbin):
    D = get_dists_of_connected_pairs(g)
    dst_max = np.sqrt(2)*g.graph_properties["ed_l"]
    frq, bins = np.histogram(D, np.linspace(0,dst_max,nbin))
    return frq

def get_L2_difference(eps_frac, gid, nbin):
    gpath = '/home/lab/data/aniso-netw_N1000' +\
            '_w37.3_ed-l296_4GX7-{:s}.gt'.format(gid)
    g = gt.load_graph(gpath)
    hpath = '/home/lab/data/rew-stat_aniso' +\
            '_rf1.00_ef{:.2f}-{:s}.gt'.format(eps_frac,gid)
    h = gt.load_graph(hpath)

    assert(g.graph_properties["ed_l"]==h.graph_properties["ed_l"])

    L2d = np.linalg.norm(cnct_dst_frq(g,nbin)-cnct_dst_frq(h,nbin))

    return L2d

    
    
#     counts = np.hist
    
#     return len(rew_stat["fail_edges"])

gids = ['9f2f']#, '2809', 'bc48']
# efracs = [0.01,0.02,0.05,0.10,0.15,0.25]
efracs = [0.05,0.5]
# nfail_mu = []
# nfail_sem = []

# gid = '9f2f'

for eps_frac in efracs:

    for gid in gids:
        print eps_frac, get_L2_difference(eps_frac, gid, 10000)
    # nfail_mu.append(np.mean(nfails))
    # nfail_sem.append(scipy.stats.sem(nfails))

    
# fig = pl.figure()
# ax = fig.add_subplot(111)
# pl.errorbar(efracs, nfail_mu, yerr=nfail_sem)
# pl.ylim(0,1200)

# import os
# fname = os.path.splitext(os.path.basename(__file__))[0]

# pl.savefig('../img/{:s}.png'.format(fname),
#            dpi=300,  bbox_inches='tight')
