
import sys, pickle, itertools
sys.path.append("..")

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import graph_tool as gt

import numpy as np
from scipy import stats

from utils.colors import color



dpath = '/home/lab/comp/data/istm_all_N1000_ngraphs1000_nbin1000.p'
with open(dpath, 'rb') as pfile:
    data = pickle.load(pfile)


matplotlib.rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    
    r'\usepackage[eulergreek]{sansmath}',   
    r'\sansmath'                
    r'\usepackage{siunitx}',    
    r'\sisetup{detect-all}',
    r'\usepackage{nicefrac}'
]  


fig = pl.figure()
fig.set_size_inches(2.8, 1.95)

ax = fig.add_subplot(111)

def norm(mean_data):
    c = 1./np.sum(mean_data*(data['centers'][2]-data['centers'][1]))
    return mean_data*c


ax.plot(data['centers'], norm(data['tuned']['mean']),
            color=color['tuned'], markersize=0, lw=1.5,
            zorder=1, label='tuned.', alpha=1)


ax.plot(data['centers'], norm(data['rew_tuned']['mean']),
            color='grey', markersize=0, lw=2,
            zorder=-0, label='rewired', alpha=1)

ax.plot(data['centers'], norm(data['dist_tuned']['mean']),
            color=color['dist'], markersize=0, lw=2,
            zorder=-0, label='dist.~dep.', alpha=1)




# ax.set_xlim(0,375)
# ax.set_ylim(0,24)
ax.set_yticks([0,10,20,30])


fig.tight_layout()

legend = ax.legend(loc='lower left', frameon=False, fontsize=12,
                   bbox_to_anchor=(0.02,0.31), handlelength=1.6,
                   handletextpad=0.6)


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

pl.ylabel("probability density", fontsize=12, labelpad=11.5)
pl.xlabel(r'aniostropy measure $\lambda$', fontsize=12, labelpad=8)


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.pdf'.format(fname), dpi=600, bbox_inches='tight')



