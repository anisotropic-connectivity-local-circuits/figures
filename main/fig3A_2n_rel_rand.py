
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import sys
sys.path.append("..")
sys.path.append("../..")

from core.neuronpair_counts import get_2neuron_counts_rel_random, get_2neuron_counts_rel_rew

from utils.colors import color


gpath_base = '/home/lab/comp/data/aniso-netw_N1000' +\
             '_w37.3_ed-l296_4GX7'

y_aniso, y_aniso_err = get_2neuron_counts_rel_random(gpath_base)


gpath_base = '/home/lab/comp/data/tuned-an-netw_N1000' +\
             '_ed-l296_XY51'

y_tuned, y_tuned_err = get_2neuron_counts_rel_random(gpath_base)



matplotlib.rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    
    r'\usepackage[eulergreek]{sansmath}',   
    r'\sansmath'                
    r'\usepackage{siunitx}',    
    r'\sisetup{detect-all}',    
]  


pl.rcParams['xtick.major.pad']='45'

fig = pl.figure(facecolor="white")
fig.set_size_inches(2.3*4./3,2.25)
ax = fig.add_subplot(111) 

ax.set_xlim(0.,3.8)
ax.set_ylim(0.825,2.15)

ax.spines['bottom'].set_position(('data',1))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([1.0,1.5,2.0])

x_aniso = [0.2,1.4,2.6]
x_tuned = [x+0.5 for x in x_aniso]

lw = 4.
opacity = 0.6
bwidth = 0.45

aniso_patches = ax.bar(x_aniso, y_aniso-1, bwidth, linewidth=lw,
                       bottom = 1., edgecolor=color['aniso'],
                       facecolor = 'white', zorder=1, yerr=y_aniso_err,
                       error_kw=dict(ecolor=color['aniso'], lw=3,
                                     capsize=5, capthick=1, mew = 2))

aniso_fill = ax.bar(x_aniso, y_aniso-1, bwidth, bottom = 1., edgecolor=color['aniso'], facecolor = color['aniso'], alpha=opacity,  zorder = 2)

tuned_patches = ax.bar(x_tuned, y_tuned-1, bwidth, linewidth=lw, bottom = 1., edgecolor=color['tuned'], facecolor = 'white', zorder=1, yerr=y_tuned_err,
                       error_kw=dict(ecolor=color['tuned'], lw=3,
                                     capsize=5, capthick=1, mew = 2))

tuned_fill = ax.bar(x_tuned, y_tuned-1, bwidth, bottom = 1., edgecolor=color['tuned'], facecolor = color['tuned'], alpha=opacity,  zorder = 2)



def correct_bar_sizes(xs, ys, patches):

    clip_boxes = [pl.Rectangle([x,0], bwidth, y,) for x,y in zip(xs,ys)]

    for clip_box,bar in zip(clip_boxes,patches):
        bar.set_clip_path(clip_box.get_path(), bar.get_transform())


correct_bar_sizes(x_aniso, y_aniso-1, aniso_patches)
correct_bar_sizes(x_aniso, y_aniso-1, aniso_fill)

correct_bar_sizes(x_tuned, y_tuned-1, tuned_patches)
correct_bar_sizes(x_tuned, y_tuned-1, tuned_fill)




# ---------------- custom legend -------------------
#
# for aniso. and tuned networks
#

from matplotlib.patches import Rectangle

xrect = 0.35
yrect1 = 1.96
rect_w = 0.06
rect_len = 0.4

yrect2 = 1.79

ax.add_patch(Rectangle((xrect,yrect1), rect_len, rect_w, edgecolor = color['tuned'], facecolor='white', lw=1.25)) 
ax.add_patch(Rectangle((xrect,yrect1), rect_len, rect_w, edgecolor = color['tuned'], facecolor=color['tuned'], alpha=opacity))
fig.text(0.315,0.78, r'tuned anisotropic', color = 'black', fontsize=11) 

ax.add_patch(Rectangle((xrect,yrect2), rect_len, rect_w, facecolor = 'white', edgecolor=color['aniso'], lw=1.25))
ax.add_patch(Rectangle((xrect,yrect2), rect_len, rect_w, facecolor = color['aniso'], edgecolor=color['aniso'], alpha=opacity))
fig.text(0.315,0.68, r'anisotropic', color = 'black', fontsize=11)





# ---------------- arrow markers as xlabels -------------------
# see http://stackoverflow.com/a/22244714/692634,
# http://matplotlib.org/examples/pylab_examples/arrow_simple_demo.html
#
# mew = markeredgewith
#
# clip_on=False allows plotting outside the x- and y-axis

ypos = 0.65
ndist = 0.6
msize = 8
left_in = 0.2
right_in = 0.2
mew_set = 1.2
awidth = 0.001
hwidth = 0.05
yoffset = 0.025

#  0    O 
start = 0.2
ax.plot(start+left_in,ypos,'o',markersize=msize, color = 'white',
        mew=mew_set, clip_on=False)
ax.plot(start+left_in+ndist, ypos, 'bo', markersize=msize,
        color='white', mew=mew_set, clip_on=False)

#  0--->O 
start = 1.4
ax.plot(start+left_in,ypos,'bo',markersize=msize,
        color='white', mew=mew_set, clip_on=False)
ax.plot(start+left_in+ndist, ypos, 'bo', markersize=msize,
        color='white', mew=mew_set, clip_on=False)
ax.arrow(start+left_in,ypos, ndist-0.2, 0, width=awidth, fc='k', ec='k',
         head_width=hwidth, head_length=0.1, clip_on=False)

#  0<-->O 
start = 2.6
ax.plot(start+left_in,ypos,'o', markersize=msize, color='white',
        mew=mew_set, clip_on=False)
ax.plot(start+left_in+ndist, ypos, 'bo', markersize=msize,
        color='white', mew=mew_set, clip_on=False)
ax.arrow(start+left_in,ypos+yoffset, ndist-0.2, 0, head_width=hwidth,
         head_length=0.1, fc='k', ec='k', clip_on=False)
ax.arrow(start+left_in+ +ndist ,ypos-yoffset, -ndist+0.2, 0,
         head_width=hwidth, head_length=0.1, fc='k', ec='k', clip_on=False)

        
ax.set_ylabel(r'counts in aniso.~net.'+'\n'+r'relative to random')



path = "fig3A_2n_rel_rand.png"
pl.savefig(path, dpi=300, bbox_inches='tight')
pl.close('all')
