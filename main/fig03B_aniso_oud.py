
import sys, pickle, itertools
sys.path.append("..")

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import graph_tool as gt

import numpy as np
from scipy import stats

from utils.colors import color



dpath = '/home/lab/comp/data/degree_distribution_all_N1000_ngraphs1000.p'
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


ax.plot(data['bin_vals'], data['out']['aniso']['mean'],
            color=color['aniso'], markersize=0, lw=2,
            zorder=-2, label='aniso.', alpha=1)

ax.plot(data['bin_vals'], data['out']['rew_aniso']['mean'],
            color=color['rew'], markersize=0, lw=2,
            zorder=-1, label='rewired', alpha=1, dashes=[3.75,4.75])

# ax.plot(data['bin_vals'], data['out']['rew10_aniso']['mean'],
#             color='grey', markersize=0, lw=2,
#             zorder=-0, label='dist.~dep.', alpha=1)

ax.plot(data['bin_vals'], data['out']['dist_aniso']['mean'],
            color=color['dist'], markersize=0, lw=2,
            zorder=-3, label='dist.~dep.', alpha=1)



# dpath = '/home/lab/comp/this.p'
# with open(dpath, 'rb') as pfile:
#     data = pickle.load(pfile)

# ax.plot(data['bin_vals'], data['out']['random']['mean'],
#             color='black', markersize=0, lw=2,
#             zorder=-8, label='random', alpha=1, dashes=[3,4])


x = data['bin_vals']
y = [999*stats.binom.pmf(k, n=999,
                     p=0.116) for k in data['bin_vals']]
ax.plot(x, y, markersize=0, lw=2, zorder=-11,
        color='grey', label='random', alpha=0.85)




ax.set_xlim(0,375)
ax.set_ylim(0,41)
ax.set_xticks([0,100,200,300])
ax.set_yticks([0,10,20,30,40])



fig.tight_layout()

legend = ax.legend(loc='lower left', frameon=False, fontsize=12,
                   bbox_to_anchor=(0.39,0.21), handlelength=2.22,
                   handletextpad=0.6)



ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

pl.ylabel("occurrence", fontsize=12, labelpad=11.5)
pl.xlabel(r'out-degree', fontsize=12, labelpad=8)


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.pdf'.format(fname), dpi=600, bbox_inches='tight')



