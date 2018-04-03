
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import sys
sys.path.append("..")
sys.path.append("../..")

from core.neuronpair_counts import get_2neuron_counts_rel_random

from utils.colors import color


gpath_base = '/home/lab/comp/data/aniso-netw_N1000' +\
             '_w37.3_ed-l296_4GX7'

y_aniso, y_aniso_err = get_2neuron_counts_rel_random(gpath_base)


gpath_base = '/home/lab/comp/data/tuned-an-netw_N1000' +\
             '_ed-l296_XY51'

y_tuned, y_tuned_err = get_2neuron_counts_rel_random(gpath_base)


# cp = np.zeros(5)
# ps = np.zeros((5,3))

# for gid in range(5):
#     # gpath = '/home/lab/comp/data/aniso-netw_N1000' +\
#     #         '_w37.3_ed-l296_4GX7-{:02d}.gt'.format(gid)
#     gpath = '/home/lab/comp/data/tuned-an-netw_N1000' +\
#             '_ed-l296_XY51-{:02d}.gt'.format(gid)
#     g = gt.load_graph(gpath)
#     cp[gid] += eval_connectivity(g)
#     ps[gid,:] += get_2neuron_p(g)


# y = [np.mean(rl_uc)-1, np.mean(rl_sp)-1, np.mean(rl_rc)-1]
# y_err = [scipy_sem(rl_uc), scipy_sem(rl_sp), scipy_sem(rl_rc)]



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
ax = fig.add_subplot(111) #aspect = 'equal')
#ax.grid(True)     

ax.set_xlim(0.,3.8)
ax.set_ylim(0.825,2.15) #1.75
#ax.set_ylim(0.9,1.1)


ax.spines['bottom'].set_position(('data',1))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([1.0,1.5,2.0])

x_aniso = [0.2,1.4,2.6]
x_tuned = [x+0.5 for x in x_aniso]
#y = [uc_org/uc_dist-1., sc_org/sc_dist-1., rc_org/rc_dist-1.]
#y = [uc_org/uc_rew-1., sc_org/sc_rew-1., rc_org/rc_rew-1.]
#y = [uc_dist/uc_rew-1., sc_dist/sc_rew-1., rc_dist/rc_rew-1.]

# ax.bar(xbar, y, 1., bottom = 1., facecolor='black', #edgecolor = 'gray' ,
#        yerr=y_err, error_kw=dict(ecolor='red', lw=2, capsize=5, capthick=1, mew = 2))


lw = 4.
opacity = 0.6
bwidth = 0.45

aniso_patches = ax.bar(x_aniso, y_aniso-1, bwidth, linewidth=lw, bottom = 1., edgecolor=color['aniso'], facecolor = 'white', zorder=1)

aniso_fill = ax.bar(x_aniso, y_aniso-1, bwidth, bottom = 1., edgecolor=color['aniso'], facecolor = color['aniso'], alpha=opacity,  zorder = 2)

tuned_patches = ax.bar(x_tuned, y_tuned-1, bwidth, linewidth=lw, bottom = 1., edgecolor=color['tuned'], facecolor = 'white', zorder=1)

tuned_fill = ax.bar(x_tuned, y_tuned-1, bwidth, bottom = 1., edgecolor=color['tuned'], facecolor = color['tuned'], alpha=opacity,  zorder = 2)



def correct_bar_sizes(xs, ys, patches):

    clip_boxes = [pl.Rectangle([x,0], bwidth, y,) for x,y in zip(xs,ys)]

    for clip_box,bar in zip(clip_boxes,patches):
        bar.set_clip_path(clip_box.get_path(), bar.get_transform())


correct_bar_sizes(x_aniso, y_aniso-1, aniso_patches)
correct_bar_sizes(x_aniso, y_aniso-1, aniso_fill)

correct_bar_sizes(x_tuned, y_tuned-1, tuned_patches)
correct_bar_sizes(x_tuned, y_tuned-1, tuned_fill)






#pl.errorbar([x+0.5 for x in xbar],[yval+1 for yval in y], yerr=y_err, color = 'r', fmt='.')
#ax.set_xlabel("unconnected - single connections - reciprocal connections")
#ax.set_ylabel("Counts relative to random")
#ax.set_title(r'relative to random')



#pl.xlim(-0.025,1.025)
#pl.yticks(np.arange(1.92,2.02,0.03))

#pl.xlabel("rewiring fraction", labelpad = 8.)
#pl.ylabel("average path length", labelpad = 14.)
#pl.title(r'\textbf{average path length}',  y=1.05, fontdict = {'size':17, 'weight':'bold'})

fig = pl.gcf()
fig.set_size_inches(2.3*4./3,2.25)
fig.tight_layout()




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

# fig.text(0.41,0.625, "anisotropic", color = 'b')
# fig.text(0.35,0.24, "distance-dependent", color = 'r')

path = "fig3_2n.png"
pl.savefig(path, dpi=300, bbox_inches='tight')
pl.close('all')
