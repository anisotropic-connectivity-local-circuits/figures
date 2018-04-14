
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import numpy as np
from scipy.stats import sem as scipy_sem

import sys
sys.path.append("..")
sys.path.append("../..")

from core.neuronpair_counts import get_2neuron_counts_abs, get_2neuron_ps

from utils.colors import color
from utils.other import correct_bars


gpath_base      = '/home/lab/comp/data/aniso-netw_N1000' +\
                  '_w37.3_ed-l296_4GX7'
gpath_base_dist = '/home/lab/comp/data/dist-an-netw_N1000' +\
                  '_w37.3_ed-l296_8CY2'
gpath_base_rew  = '/home/lab/comp/data/rew-netw_rfrac1.00' +\
                  '_efrac0.05_4FU2'

p_aniso, p_rnd = get_2neuron_ps(gpath_base)
p_dist, _ = get_2neuron_ps(gpath_base_dist)
p_rew, _ = get_2neuron_ps(gpath_base_rew)


matplotlib.rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    
    r'\usepackage[eulergreek]{sansmath}',   
    r'\sansmath'                
    r'\usepackage{siunitx}',    
    r'\sisetup{detect-all}',    
]  

fig = pl.figure(facecolor="white")
fig.set_size_inches(1.8*2.3*4./3,2.12)
ax1 = fig.add_subplot(131)
ax2 = fig.add_subplot(132)
ax3 = fig.add_subplot(133)
axs = [ax1, ax2, ax3]

for ax in axs:
    # ax.spines['bottom'].set_position(('data',1))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.xaxis.set_ticks([])
    ax.set_xlim(0.,1.)
    ax.set_ylim(bottom=0.)


# ax.set_xlim(0.,3.8)
# ax.set_ylim(0.825,2.15)

# ax.xaxis.set_ticks([])
# ax.yaxis.set_ticks([1.0,1.5,2.0])


# x_tuned = [x+0.5 for x in x_aniso]

lw = 3.
opacity = 0.6

xlocs = [0.125,0.325,0.525,0.725]
bwidth = 0.135

for k,ax in enumerate(axs):

    aniso_patch = ax.bar(xlocs[0], np.mean(p_aniso, axis=0)[k],
                         bwidth, linewidth=lw,
                         edgecolor=color['aniso'],
                         facecolor = 'white', zorder=1,
                         yerr=scipy_sem(p_aniso, axis=0)[k],
                         error_kw=dict(ecolor=color['aniso'], lw=3,
                                       capsize=5, capthick=1, mew = 2))

    aniso_fill = ax.bar(xlocs[0], np.mean(p_aniso, axis=0)[k],
                        bwidth, edgecolor=color['aniso'],
                        facecolor = color['aniso'], alpha=opacity,  zorder = 2)

    rew_patch = ax.bar(xlocs[1], np.mean(p_rew, axis=0)[k],
                         bwidth, linewidth=lw,
                         edgecolor=color['rew'],
                         facecolor = 'white', zorder=1,
                         yerr=scipy_sem(p_rew, axis=0)[k],
                         error_kw=dict(ecolor=color['rew'], lw=3,
                                       capsize=5, capthick=1, mew = 2))

    rew_fill = ax.bar(xlocs[1], np.mean(p_rew, axis=0)[k],
                        bwidth, edgecolor=color['rew'],
                        facecolor = color['rew'], alpha=opacity,  zorder = 2)
    
    dist_patch = ax.bar(xlocs[2], np.mean(p_dist, axis=0)[k],
                         bwidth, linewidth=lw,
                         edgecolor=color['dist'],
                         facecolor = 'white', zorder=1,
                         yerr=scipy_sem(p_dist, axis=0)[k],
                         error_kw=dict(ecolor=color['dist'], lw=3,
                                       capsize=5, capthick=1, mew = 2))

    dist_fill = ax.bar(xlocs[2], np.mean(p_dist, axis=0)[k],
                        bwidth, edgecolor=color['dist'],
                        facecolor = color['dist'], alpha=opacity,  zorder = 2)


    rnd_patch = ax.bar(xlocs[3], np.mean(p_rnd, axis=0)[k],
                         bwidth, linewidth=lw,
                         edgecolor=color['rnd'],
                         facecolor = 'white', zorder=1,
                         yerr=scipy_sem(p_rnd, axis=0)[k],
                         error_kw=dict(ecolor=color['rnd'], lw=3,
                                       capsize=5, capthick=1, mew = 2))

    rnd_fill = ax.bar(xlocs[3], np.mean(p_rnd, axis=0)[k],
                        bwidth, edgecolor=color['rnd'],
                        facecolor = color['rnd'], alpha=opacity,  zorder = 2)

    
    correct_bars([xlocs[0]], [np.mean(p_aniso, axis=0)[k]], aniso_patch, bwidth)
    correct_bars([xlocs[0]], [np.mean(p_aniso, axis=0)[k]], aniso_fill, bwidth)

    correct_bars([xlocs[1]], [np.mean(p_rew, axis=0)[k]], rew_patch, bwidth)
    correct_bars([xlocs[1]], [np.mean(p_rew, axis=0)[k]], rew_fill, bwidth)

    correct_bars([xlocs[2]], [np.mean(p_dist, axis=0)[k]], dist_patch, bwidth)
    correct_bars([xlocs[2]], [np.mean(p_dist, axis=0)[k]], dist_fill, bwidth)

    correct_bars([xlocs[3]], [np.mean(p_rnd, axis=0)[k]], rnd_patch, bwidth)
    correct_bars([xlocs[3]], [np.mean(p_rnd, axis=0)[k]], rnd_fill, bwidth)
    
    
    
# ---------------- custom legend -------------------
#
# for aniso. and tuned networks
#

from matplotlib.patches import Rectangle

xrect = .95
yrect1 = 0.020
rect_w = 0.006
rect_len = 0.4

yrect2 = 1.79

xtext = 1.075
ytext_start = 0.78
ytext_sep = 0.15

ax3.add_patch(Rectangle((xrect,yrect1), rect_len, rect_w, edgecolor = color['aniso'], facecolor='white', lw=1.25, clip_on=False)) 
ax3.add_patch(Rectangle((xrect,yrect1), rect_len, rect_w, edgecolor = color['aniso'], facecolor=color['aniso'], alpha=opacity, clip_on=False))

fig.text(xtext,ytext_start, r'aniso.', color = 'black', fontsize=11)
fig.text(xtext,ytext_start-ytext_sep, r'rewired', color = 'black', fontsize=11)
fig.text(xtext,ytext_start-2*ytext_sep, r'dist.~depend.', color = 'black', fontsize=11) 
fig.text(xtext,ytext_start-3*ytext_sep, r'random', color = 'black', fontsize=11) 


ax3.add_patch(Rectangle((xrect,yrect2), rect_len, rect_w, facecolor = 'white', edgecolor=color['aniso'], lw=1.25))
ax3.add_patch(Rectangle((xrect,yrect2), rect_len, rect_w, facecolor = color['aniso'], edgecolor=color['aniso'], alpha=opacity))






# ---------------- arrow markers as xlabels -------------------
# see http://stackoverflow.com/a/22244714/692634,
# http://matplotlib.org/examples/pylab_examples/arrow_simple_demo.html
#
# mew = markeredgewith
#
# clip_on=False allows plotting outside the x- and y-axis

ypos = -0.35
ndist = 0.45
msize = 10.5
left_in = 0.1
right_in = 0.1
mew_set = 1.6
awidth = 0.001
hwidth = 0.01
yoffset = 0.00065

f3A_ymax=1.325

ax1_ymax=0.85
y1pos = ax1_ymax/f3A_ymax*ypos
ax2_ymax=0.23
y2pos = ax2_ymax/f3A_ymax*ypos
ax3_ymax=0.027
y3pos = ax3_ymax/f3A_ymax*ypos

awidth2 =ax2_ymax/f3A_ymax*awidth
awidth3 =ax3_ymax/f3A_ymax*awidth 


#  0    O 
start = 0.15
ax1.plot(start+left_in,y1pos,'o',markersize=msize, color = 'white',
        mew=mew_set, clip_on=False)
ax1.plot(start+left_in+ndist, y1pos, 'bo', markersize=msize,
        color='white', mew=mew_set, clip_on=False)

# #  0--->O 
ax2.plot(start+left_in,y2pos,'bo',markersize=msize,
        color='white', mew=mew_set, clip_on=False)
ax2.plot(start+left_in+ndist, y2pos, 'bo', markersize=msize,
        color='white', mew=mew_set, clip_on=False)
ax2.arrow(start+left_in,y2pos, ndist-0.2, 0, width=awidth2, fc='k', ec='k',
         head_width=hwidth, head_length=0.1, clip_on=False)

#  0<-->O 
ax.plot(start+left_in,y3pos,'o', markersize=msize, color='white',
        mew=mew_set, clip_on=False)
ax.plot(start+left_in+ndist, y3pos, 'bo', markersize=msize,
        color='white', mew=mew_set, clip_on=False)
ax.arrow(start+left_in,y3pos+yoffset, ndist-0.2, 0, head_width=hwidth/10.,
         head_length=0.1, fc='k', ec='k', clip_on=False, width=awidth3)
ax.arrow(start+left_in+ ndist ,y3pos-yoffset, -ndist+0.2, 0,
         head_width=hwidth/10., head_length=0.1, fc='k', ec='k', clip_on=False,
         width=awidth3)


ax1.set_ylabel(r'relative occurrence of'+'\n'+r'two neuron motif')

ax1.set_ylim(top=ax1_ymax)
ax2.set_ylim(top=ax2_ymax)
ax3.set_ylim(top=ax3_ymax)

ax1.set_yticks([0.,0.2,0.4,0.6,0.8])

pl.tight_layout()

path = "fig3B_2n_rel_occurrence.png"
pl.savefig(path, dpi=300, bbox_inches='tight')
pl.close('all')
