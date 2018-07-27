
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


dpath = '/home/lab/comp/data/cinp_dstrb'+\
        '_tuned_N1000_ed-l296_ngraph1000.p'
with open(dpath, 'rb') as pfile:
    ci_tuned = pickle.load(pfile)

   

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


ax.plot(ci_tuned['centers'], ci_tuned['unc_means'],
        color=color['tuned'], markersize=0, lw=2,
        zorder=-0, label='unconnected', alpha=0.5)
ax.plot(ci_tuned['centers'], ci_tuned['sng_means'],
        color=color['tuned'], markersize=0, lw=2, zorder=-1,
        label=r'undirectional', dashes=[3,2], alpha=0.75)
ax.plot(ci_tuned['centers'], ci_tuned['bdr_means'],
        color=color['tuned'], markersize=0, lw=2,
        zorder=-2, label='bidirectional')    
    

ax.set_xlim(0,100)
ax.set_ylim(0,0.075)
ax.set_xticks([0,20,40,60,80,100])
ax.set_yticks([0,0.02,0.04,0.06])

fig.tight_layout()

legend = ax.legend(loc='lower left', frameon=False, fontsize=12,
                   bbox_to_anchor=(0.34,0.21), handlelength=2.1,
                   handletextpad=0.6, title='tuned anisotropic')
for text in legend.texts:
    text.set_visible(False)  # disable label


#    o       o
#    o ----> o
#    o <---> o
x1, x2 = 55.5,66.5
ypos, ystep = 0.0555, -0.01305
mew_set = 1
msize = 5

arrow_xpad = 2.75
arrow_ypad = 0.0015
arrow_headlength = 1.2
arrow_width = 0.0001
arrow_hwidth = 0.0015

ax.plot(x1, ypos, 'o', markersize=msize,
        color='white', mew=mew_set, clip_on=False) 
ax.plot(x2, ypos,'o',markersize=msize,
        color='white', mew=mew_set, clip_on=False)

ax.plot(x1, ypos+ystep, 'o', markersize=msize,
        color='white', mew=mew_set, clip_on=False) 
ax.plot(x2, ypos+ystep,'o',markersize=msize,
        color='white', mew=mew_set, clip_on=False)
ax.arrow(x=x1+arrow_xpad, y=ypos+ystep,
         dx=x2-x1-2*arrow_xpad, dy=0, 
         width=arrow_width, head_width=arrow_hwidth,
         head_length=arrow_headlength, fc='k', ec='k',
         length_includes_head=True, clip_on=False)


ax.plot(x1, ypos+2*ystep, 'o', markersize=msize,
        color='white', mew=mew_set, clip_on=False) 
ax.plot(x2, ypos+2*ystep,'o',markersize=msize,
        color='white', mew=mew_set, clip_on=False)
ax.arrow(x=x1+arrow_xpad, y=ypos+2*ystep+arrow_ypad,
         dx=x2-x1-2*arrow_xpad, dy=0, 
         width=arrow_width, head_width=arrow_hwidth,
         head_length=arrow_headlength, fc='k', ec='k',
         length_includes_head=True, clip_on=False)
ax.arrow(x=x2-arrow_xpad, y=2*ystep+ypos-arrow_ypad,
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



