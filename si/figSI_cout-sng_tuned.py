
import sys, pickle, itertools
sys.path.append("..")
sys.path.append("../../")
sys.path.append("../../comp/functions/")

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import graph_tool as gt

import numpy as np
from scipy import stats

from network_eval import get_common_neighbours

from utils.colors import color


plot, ngraphs, binw = True, 5, 1

bins = np.arange(0,1000+binw,binw)
centers = 0.5*(bins[1:]+bins[:-1])

in_tuned_bdr  = np.zeros((ngraphs, len(bins)-1))
in_r025tuned_bdr  = np.zeros((ngraphs, len(bins)-1))
in_rtuned_bdr  = np.zeros((ngraphs, len(bins)-1))


for gid in range(ngraphs):
    if plot:

        gpath = '/home/lab/comp/data/tuned-an-netw_N1000' +\
                '_ed-l296_XY51-{:02d}.gt'.format(gid)
        g = gt.load_graph(gpath)
        pairs, cn, in_nb, out_nb = get_common_neighbours(g)
        in_tuned_bdr[gid,:]+=np.histogram(out_nb[cn==1], bins,
                                          density=True)[0]

        gpath = '/home/lab/comp/data/rew_tuned_netw' +\
                '_rfrac0.25_efrac0.05-{:02d}.gt'.format(gid)
        g = gt.load_graph(gpath)
        pairs, cn, in_nb, out_nb = get_common_neighbours(g)
        in_r025tuned_bdr[gid,:]+=np.histogram(out_nb[cn==1], bins,
                                              density=True)[0]

        gpath = '/home/lab/comp/data/rew_tuned_netw' +\
                '_rfrac1.00_efrac0.05-{:02d}.gt'.format(gid)
        g = gt.load_graph(gpath)
        pairs, cn, in_nb, out_nb = get_common_neighbours(g)
        in_rtuned_bdr[gid,:]+=np.histogram(out_nb[cn==1], bins,
                                           density=True)[0]
        

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


 
if plot:
    ax.plot(centers, np.mean(in_tuned_bdr, axis=0),
            color=color['tuned'], markersize=0, lw=2,
            zorder=-0, label='tuned')
    ax.plot(centers, np.mean(in_r025tuned_bdr, axis=0),
            color='grey', markersize=0, lw=2, zorder=-1,
            label=r'$\nicefrac{1}{4}$ rewired')
    ax.plot(centers, np.mean(in_rtuned_bdr, axis=0),
            color=color['rew'], markersize=0, lw=2,
            zorder=-2, label='rewired')
else:
    ax.plot([0], [0],
            color=color['tuned'], markersize=0, lw=2,
            zorder=-0, label='tuned')
    ax.plot([0],[0],
            color='grey', markersize=0, lw=2, zorder=-1,
            label=r'$\nicefrac{1}{4}$ rewired')
    ax.plot([0],[0],
            color=color['rew'], markersize=0, lw=2,
            zorder=-2, label='rewired')


ax.set_xlim(0,100)
ax.set_ylim(0,0.075)
ax.set_xticks([0,20,40,60,80,100])
ax.set_yticks([0,0.02,0.04,0.06])

#          
#    o <---> 0
#
x1, x2 = 47.5,62.5
ypos = 0.075
mew_set = 1
msize = 5

arrow_xpad = 2.75
arrow_ypad = 0.0015
arrow_headlength = 2.5
arrow_width = 0.0001
arrow_hwidth = 0.0025

ax.plot(x1, ypos, 'o', markersize=msize,
        color='white', mew=mew_set, clip_on=False) 
ax.plot(x2, ypos,'o',markersize=msize,
        color='white', mew=mew_set, clip_on=False)
ax.arrow(x=x1+arrow_xpad, y=ypos,
         dx=x2-x1-2*arrow_xpad, dy=0, 
         width=arrow_width, head_width=arrow_hwidth,
         head_length=arrow_headlength, fc='k', ec='k',
         length_includes_head=True, clip_on=False)


fig.tight_layout()

ax.legend(loc='lower left', frameon=False, fontsize=12,
          bbox_to_anchor=(0.31,0.3), handlelength=1.9,
          handletextpad=0.6)


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

pl.ylabel("probability density", fontsize=12, labelpad=11.5)
pl.xlabel(r'common outputs', fontsize=12, labelpad=8)


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.pdf'.format(fname), dpi=600, bbox_inches='tight')



ax.errorbar(centers, np.mean(in_tuned_bdr, axis=0),
            yerr=stats.sem(in_tuned_bdr,axis=0), capsize=1,
            color=color['tuned'], fmt='.', markersize=0, lw=1,
            zorder=-0)
ax.errorbar(centers, np.mean(in_r025tuned_bdr, axis=0),
            yerr=stats.sem(in_r025tuned_bdr,axis=0), capsize=1,
            color='grey', fmt='.', markersize=0, lw=1, zorder=-1)
ax.errorbar(centers, np.mean(in_rtuned_bdr, axis=0),
            yerr=stats.sem(in_rtuned_bdr,axis=0), capsize=1,
            color=color['rew'], fmt='.', markersize=0, lw=1,
            zorder=-2)    
    
pl.savefig('{:s}_{:s}.pdf'.format(fname,'errors'), dpi=600,
           bbox_inches='tight')
