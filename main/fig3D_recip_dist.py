
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
from comp.functions import Tuned_netw_dist_profile, get_dd_recip_p

from data.extract_recip_p import xvals_data as Perin2011_x
from data.extract_recip_p import yvals_data as Perin2011_y
from data.extract_recip_p import yerrs_data as Perin2011_yerr


Tuned_netw_dist_profile = Tuned_netw_dist_profile()

xs = np.arange(0,418.6,0.01)
dd_recip_ps = np.array([Tuned_netw_dist_profile.ddcp(x)**2 for x in xs])

def pr_fit(x):

    a = -1.2451623637345335E-01
    b = 9.2442483915416082E-03
    c = 1.1041322663714865E+00
    offset = 1.2326119868850784E-01

    return a * math.pow(1.0 - math.exp(-1.0 * b * x), c) + offset

Perin2011_pfit = np.array([pr_fit(x) for x in xs])


bins = np.linspace(0,296*np.sqrt(2),12)
tP = []

for gid in range(3):
    tpath = '/home/lab/comp/data/tuned-an-netw' +\
            '_N1000_ed-l296_XY51-{:02d}.gt'.format(gid)
    t = gt.load_graph(tpath)
    t_ctrs, t_ps = get_dd_recip_p(t, bins)
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

ax.plot(xs, dd_recip_ps, dashes=[2,2], color=color['tuned'])
ax.plot(xs, Perin2011_pfit, color='grey')
ax.errorbar(Perin2011_x, Perin2011_y, yerr=Perin2011_yerr,
            fmt='.', color='grey', capsize=0)
ax.errorbar(t_ctrs, np.mean(tP, axis=0), yerr=stats.sem(tP, axis=0),
            fmt='o', markeredgecolor=color['tuned'],
            markerfacecolor='None', ecolor='None', markersize=3.5,
            markeredgewidth=1)

ymin, ymax = 0, 0.135
ax.set_ylim(ymin,ymax)
ax.set_xlim(0,418.6)

ax.set_xticks([0,100,200,300,400])
ax.set_yticks(np.arange(0, ymax, 0.03))

fig.tight_layout()


#          
#    o <---> 0
#
mew_set = 1.2
msize = 8
ypos = 0.195/0.25*(ymax-ymin)
awidth = 0.001/0.25*(ymax-ymin)
hwidth = 0.01/0.25*(ymax-ymin)

ax.plot(290, ypos, 'o', markersize=msize,
        color='white', mew=mew_set) 
ax.plot(370, ypos,'o',markersize=msize,
        color='white', mew=mew_set)
ax.arrow(307.5, ypos+0.0025, 52-17.5, 0, 
         width=awidth, head_width=hwidth,
         head_length=10, fc='k', ec='k')
ax.arrow(307.5+(52-17.5)+10,ypos-0.0025, -(52-17.5) , 0, 
         width=awidth, head_width=hwidth,
         head_length=10, fc='k', ec='k')



#
# custom legend
#
x_in, fontsize = 530, 11
y_start, y_lb, y_pb = 0.25/2, 0.0375/2, 0.055/2


ax.text(x_in, y_start,  'reciprocal probabilities',
        clip_on=False, size=fontsize)
ax.text(x_in, y_start-y_lb, 'from Perin et al.~(2011)', 
        clip_on=False, size=fontsize)
ax.text(x_in, y_start-y_lb-y_pb, 'fit to experimental data',
        clip_on=False, size=fontsize)
ax.text(x_in, y_start-y_lb-2*y_pb, 'expectation in dist.~',
        clip_on=False, size=fontsize)
ax.text(x_in, y_start-2*y_lb-2*y_pb, '~depend.~networks $p(x)^2$',
        clip_on=False, size=fontsize)
ax.text(x_in, y_start-2*y_lb-3*y_pb, 'tuned anisotropic',
        clip_on=False, size=fontsize)


errs = ax.errorbar([480], [y_start+0.005], yerr=[0.0225/2],
                   clip_on=False, fmt='.', color='grey',
                   capsize=0)
errorbars_clip_false(ax,errs)

ax.plot([480-20, 480+20], [y_start-y_lb-y_pb+0.005]*2,
        color='grey', lw=1, clip_on=False)

ax.plot([480-20, 480+20], [y_start-y_lb-2*y_pb+0.005]*2,
        color=color['tuned'], lw=1, clip_on=False, dashes=[2,2])

errs = ax.errorbar([480], [y_start-2*y_lb-3*y_pb+0.005], yerr=[0.0225],
                   clip_on=False, fmt='o', markeredgecolor=color['tuned'],
                   markerfacecolor='None', ecolor='None', markersize=3.5,
                   markeredgewidth=1)
errorbars_clip_false(ax,errs)



ax.axvline(850, 0, 1, clip_on=False, color='white')

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

pl.ylabel("connection probability", fontsize=12, labelpad=11.5)
pl.xlabel(r'distance in \SI{}{\micro\meter}', fontsize=12, labelpad=8)

pl.savefig('fig3D_recip_dist.png', dpi=300, bbox_inches='tight')














