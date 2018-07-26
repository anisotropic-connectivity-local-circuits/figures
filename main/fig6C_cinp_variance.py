
import sys, pickle, itertools
sys.path.append("..")

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import numpy as np
from scipy import stats

from utils.colors import color


dpath = '/home/lab/comp/data/cinpvar_tuned_' +\
        'netw_nrews21_efrac0.05.p'
with open(dpath, "rb") as pfile:
    tuned_cinpv = pickle.load(pfile)

dpath = '/home/lab/comp/data/cinpvar_dist_tuned_' +\
        'netw_nrews21_efrac0.05.p'
with open(dpath, "rb") as pfile:
    dist_cinpv = pickle.load(pfile)


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


ax.errorbar(tuned_cinpv['rew_stages'],
            np.mean(tuned_cinpv['all'], axis=0),
            color=color['tuned'], markersize=0, lw=2,
            zorder=-0, label='tuned',
            yerr=stats.sem(tuned_cinpv['all'],axis=0), capsize=1)
ax.errorbar(dist_cinpv['rew_stages'],
            np.mean(dist_cinpv['all'], axis=0),
            color=color['dist'], markersize=0, lw=2,
            zorder=-0, label='dist.~dep.',
            yerr=stats.sem(dist_cinpv['all'],axis=0), capsize=1)

# ax.plot(centers, np.mean(in_r025dist_all, axis=0),
#         color='grey', markersize=0, lw=2, zorder=-1,
#         label=r'$\nicefrac{1}{4}$ rewired', dashes=[3,2])
# ax.plot(centers, np.mean(in_rdist_all, axis=0),
#         color='grey', markersize=0, lw=2,
#         zorder=-2, label='rewired')    



# ax.set_xlim(0,80)
# ax.set_ylim(0,0.1)
# ax.set_xticks([0,20,40,60,80])
# ax.set_yticks([0,0.03,0.06,0.09])

fig.tight_layout()

ax.legend(loc='lower left', frameon=False, fontsize=12,
          bbox_to_anchor=(0.31,0.3), handlelength=1.65,
          handletextpad=0.6)


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

pl.ylabel("common input variance", fontsize=12, labelpad=11.5)
pl.xlabel(r'rewiring fraction $\eta$', fontsize=12, labelpad=8)


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.pdf'.format(fname), dpi=600, bbox_inches='tight')



