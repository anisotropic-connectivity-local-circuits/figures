
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


plot, ngraphs, binw = True, 1, 1

bins = np.arange(0,1000+binw,binw)
centers = 0.5*(bins[1:]+bins[:-1])

in_dist_unc  = np.zeros((ngraphs, len(bins)-1))
in_dist_sng  = np.zeros((ngraphs, len(bins)-1))
in_dist_bdr  = np.zeros((ngraphs, len(bins)-1))


for gid in range(ngraphs):
    if plot:

        # gpath = '/home/lab/comp/data/dist-an-netw_N1000_w37.3' +\
        #         '_ed-l296_8CY2-{:02d}.gt'.format(gid)
        gpath = '/home/lab/comp/data/dist-tuned-netw' +\
                '_N1000_ed-l296_XUI7-{:02d}.gt'.format(gid)
        g = gt.load_graph(gpath)
        pairs, cn, in_nb, out_nb = get_common_neighbours(g)
        in_dist_unc[gid,:]+=np.histogram(in_nb[cn==0], bins, density=True)[0]
        in_dist_sng[gid,:]+=np.histogram(in_nb[cn==1], bins, density=True)[0]
        in_dist_bdr[gid,:]+=np.histogram(in_nb[cn==2], bins, density=True)[0]
        

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
fig.set_size_inches(2.8*1.5, 1.95)

ax = fig.add_subplot(111)


 
if plot:
    ax.plot(centers, np.mean(in_dist_unc, axis=0),
            color=color['dist'], markersize=0, lw=2,
            zorder=-0, label='dist.~dep.', alpha=0.5)
    ax.plot(centers, np.mean(in_dist_sng, axis=0),
            color=color['dist'], markersize=0, lw=2, zorder=-1,
            label=r'$\nicefrac{1}{4}$ rewired',
            dashes=[3,2], alpha=0.75)
    ax.plot(centers, np.mean(in_dist_bdr, axis=0),
            color=color['dist'], markersize=0, lw=2,
            zorder=-2, label='rewired')    


ax.set_xlim(0,80)
ax.set_ylim(0,0.1)
ax.set_xticks([0,20,40,60,80])
ax.set_yticks([0,0.03,0.06,0.09])

fig.tight_layout()

ax.legend(loc='lower left', frameon=False, fontsize=12,
          bbox_to_anchor=(0.31,0.3), handlelength=1.9,
          handletextpad=0.6)

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
ax.arrow(x=x1+arrow_xpad, y=ypos+arrow_ypad,
         dx=x2-x1-2*arrow_xpad, dy=0, 
         width=arrow_width, head_width=arrow_hwidth,
         head_length=arrow_headlength, fc='k', ec='k',
         length_includes_head=True, clip_on=False)
ax.arrow(x=x2-arrow_xpad, y=ypos-arrow_ypad,
         dx=-(x2-x1-2*arrow_xpad), dy=0, 
         width=arrow_width, head_width=arrow_hwidth,
         head_length=arrow_headlength, fc='k', ec='k',
         length_includes_head=True, clip_on=False)



ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

pl.ylabel("probability density", fontsize=12, labelpad=11.5)
pl.xlabel(r'common inputs', fontsize=12, labelpad=8)


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.pdf'.format(fname), dpi=600, bbox_inches='tight')


