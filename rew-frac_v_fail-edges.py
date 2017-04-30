
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import numpy as np

import pickle, scipy.stats

def load_data_point(eps_frac, gid):
    dpath = '/home/lab/comp/data/rew-stat_aniso' +\
            '_rf1.00_ef{:.2f}-{:s}_stat.p'.format(eps_frac,gid)
    with open(dpath, "rb") as pfile:
        rew_stat = pickle.load(pfile)
    return len(rew_stat["fail_edges"])

gids = ['0bae', '1b20', '22df']
efracs = [0.01,0.02,0.05,0.10,0.15,0.25]
nfail_mu = []
nfail_sem = []

for eps_frac in efracs:
    nfails = []
    for gid in gids:
        nfails.append(load_data_point(eps_frac, gid))
    nfail_mu.append(np.mean(nfails))
    nfail_sem.append(scipy.stats.sem(nfails))

    
fig = pl.figure()
ax = fig.add_subplot(111)
pl.errorbar(efracs, nfail_mu, yerr=nfail_sem)
pl.ylim(0,1200)

import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.png'.format(fname),
           dpi=300,  bbox_inches='tight')
