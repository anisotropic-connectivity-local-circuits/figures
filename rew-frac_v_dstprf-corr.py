
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import numpy as np

import pickle, scipy.stats

import graph_tool as gt

import sys
sys.path.append("..")

from comp.functions import get_dists_of_connected_pairs


def load_data(gpath):
    g = gt.load_graph(gpath)
    D = get_dists_of_connected_pairs(g)
    pl.hist(D, bins=50, normed=True)
    #return len(rew_stat["fail_edges"])

load_data('/home/lab/data/aniso-netw_N1000_w37.3_ed-l296_4GX7-9f2f.gt')
load_data('/home/lab/data/rew-stat_aniso_rf1.00_ef0.05-9f2f.gt')
    
# gids = ['9f2f', '2809', 'bc48']
# efracs = [0.01,0.02,0.05,0.10,0.15,0.25]
# nfail_mu = []
# nfail_sem = []

# gid = '9f2f'

# for eps_frac in efracs:
#     nfails = []
#     for gid in gids:
#         nfails.append(load_data_point(eps_frac, gid))
#     nfail_mu.append(np.mean(nfails))
#     nfail_sem.append(scipy.stats.sem(nfails))

    
# fig = pl.figure()
# ax = fig.add_subplot(111)
# pl.errorbar(efracs, nfail_mu, yerr=nfail_sem)
# pl.ylim(0,1200)

import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('../img/{:s}.png'.format(fname),
           dpi=300,  bbox_inches='tight')
