
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import numpy as np
import scipy.stats as stats
import graph_tool as gt

import sys, math
sys.path.append("..")
sys.path.append("../..")

from utils import color, errorbars_clip_false
from comp.functions import Tuned_netw_dist_profile, get_ddcp

from data.extract_overall_p import xvals_data as Perin2011_x
from data.extract_overall_p import yvals_data as Perin2011_y
from data.extract_overall_p import yerrs_data as Perin2011_yerr


Tuned_netw_dist_profile = Tuned_netw_dist_profile()

xs = np.arange(0,418.6,0.01)
ddcp = np.array([Tuned_netw_dist_profile.ddcp(x) for x in xs])


bins = np.linspace(0,296*np.sqrt(2),12)
tP = []

for gid in range(5):
    tpath = '/home/lab/comp/data/tuned-an-netw' +\
            '_N1000_ed-l296_XY51-{:02d}.gt'.format(gid)
    t = gt.load_graph(tpath)
    t_ctrs, t_ps = get_ddcp(t, bins)
    tP.append(t_ps)

print(np.mean(tP, axis=0))

matplotlib.rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    
    r'\usepackage[eulergreek]{sansmath}',   
    r'\sansmath'                
    r'\usepackage{siunitx}',    
    r'\sisetup{detect-all}',    
]  

fig = pl.figure()
fig.set_size_inches(2.8, 1.95)

ax = fig.add_subplot(111)

ax.plot(xs, ddcp, color='grey')
ax.errorbar(Perin2011_x, Perin2011_y, yerr=Perin2011_yerr,
            fmt='.', color='grey', capsize=0)
ax.errorbar(t_ctrs, np.mean(tP, axis=0), yerr=stats.sem(tP, axis=0),
            fmt='o', markeredgecolor=color['tuned'],
            markerfacecolor='None', markersize=3.5,
            markeredgewidth=1, ecolor='None')#, capsize=0)


ymin, ymax = 0, 0.25
ax.set_ylim(ymin,ymax)
ax.set_xlim(0,418.6)

ax.set_xticks([0,100,200,300,400])

fig.tight_layout()



mew_set = 1.2
msize = 8
ypos = 0.195
awidth = 0.001
hwidth = 0.01
fontsize = 12



#          ?
#    v_1 ----> v_2
#
ax.text(290,ypos-0.002,r'$\mathbf{v_1}$', size=fontsize,
        fontweight='bold', va='center', ha='center', clip_on=False) 
ax.text(374,ypos-0.002,r'$\mathbf{v_2}$', size=fontsize,
        fontweight='bold', va='center', ha='center', clip_on=False)
ax.text(330,ypos+0.02,r'\textbf{?}', size=fontsize,
        fontweight='bold', va='center', ha='center', clip_on=False)
ax.arrow(307.5,ypos, 52-17.5, 0, width=awidth,
         head_width=hwidth, head_length=10, fc='k', ec='k')


#
# custom legend
#
x_in, fontsize = 530, 11
y_start, y_lb, y_pb = 0.22, 0.0375, 0.06


errs = ax.errorbar([480], [y_start+0.01], yerr=[0.0225],
                   clip_on=False, fmt='.', color='grey',
                   capsize=0)
errorbars_clip_false(ax,errs)

ax.text(x_in, y_start, 'somatosensory cortex',
        size=fontsize, clip_on=False)
ax.text(x_in, y_start-y_lb, 'from Perin et al.~(2011)',
        size=fontsize, clip_on=False)

ax.plot([480-20, 480+20], [y_start-y_lb-y_pb+0.01]*2,
        color='grey', lw=1, clip_on=False)
ax.text(x_in, y_start-y_lb-y_pb, 'fit to cortex data $p(x)$',
        size=fontsize, clip_on=False)

errs = ax.errorbar([480], [y_start-y_lb-2*y_pb+0.01], yerr=[0.0225],
                   clip_on=False, fmt='o', markeredgecolor=color['tuned'],
                   markerfacecolor='None', ecolor='None', markersize=3.5,
                   markeredgewidth=1)
errorbars_clip_false(ax,errs)
ax.text(x_in, y_start-y_lb-2*y_pb, 'tuned anisotropic',
        size=fontsize, clip_on=False)




ax.axvline(850, 0, 1, clip_on=False, color='white')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

pl.ylabel("connection probability", fontsize=12, labelpad=11.5)
pl.xlabel(r'distance in \SI{}{\micro\meter}', fontsize=12, labelpad=8)

pl.savefig('fig3C_2n_dstprf.png', dpi=300, bbox_inches='tight')
