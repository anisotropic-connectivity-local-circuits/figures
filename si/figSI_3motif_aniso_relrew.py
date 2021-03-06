
import sys, pickle, itertools
sys.path.append("..")
sys.path.append("../../")
sys.path.append("../../comp/functions/")

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl
from matplotlib.patches import Rectangle

import numpy as np
from scipy import stats

from utils.colors import color
from utils.motif_draw import draw_motifs
from utils.other import correct_bars, align_yaxis

from core.motif_methods import motif_count_dict_to_p_array, \
                               expected_3motif_p_from_2motif_p


# loads the the 2-neuron and 3-neuron motif
# counts  for aniso, rew and dist networks

fpath = '/home/lab/comp/data/two_motif_counts_aniso.p'
with open(fpath, 'rb') as pfile:
    aniso_2motifs = pickle.load(pfile)

fpath = '/home/lab/comp/data/two_motif_counts_rew.p'
with open(fpath, 'rb') as pfile:
    aniso_rew_2motifs = pickle.load(pfile)

fpath = '/home/lab/comp/data/two_motif_counts_tuned.p'
with open(fpath, 'rb') as pfile:
    tuned_2motifs = pickle.load(pfile)



fpath = '/home/lab/comp/data/three_motif_counts_aniso_S300000.p'
with open(fpath, 'rb') as pfile:
    aniso_3motifs = pickle.load(pfile)

fpath = '/home/lab/comp/data/three_motif_counts_rew_S300000.p'
with open(fpath, 'rb') as pfile:
    aniso_rew_3motifs = pickle.load(pfile)


fpath = '/home/lab/comp/data/three_motif_counts_tuned_S300000.p'
with open(fpath, 'rb') as pfile:
    tuned_3motifs = pickle.load(pfile)

fpath = '/home/lab/comp/data/three_motif_counts_rew_tuned_S300000.p'
with open(fpath, 'rb') as pfile:
    tuned_rew_3motifs = pickle.load(pfile)
    

    

def rel_counts_from_data(net_2motifs, aniso_net_3motifs, rew_net_3motifs):
    '''
    get the occurrence of three motifs relative to
    expected three motifs from two motif occurrence
    '''
    net_2motif_p = motif_count_dict_to_p_array(net_2motifs)
    
    exp_3motif_p = []
    for up,sp,rp in net_2motif_p:
        p_3motif = expected_3motif_p_from_2motif_p(up, sp, rp)
        exp_3motif_p.append(p_3motif)
        
    net_3motif_p = motif_count_dict_to_p_array(aniso_net_3motifs)-\
                   motif_count_dict_to_p_array(rew_net_3motifs)

    rel_counts = net_3motif_p/np.array(exp_3motif_p)

    return np.mean(rel_counts,axis=0), stats.sem(rel_counts, axis=0)
                   

rlc_aniso, errs_aniso = rel_counts_from_data(aniso_2motifs, aniso_3motifs, aniso_rew_3motifs)
rlc_tuned, errs_tuned = rel_counts_from_data(tuned_2motifs, tuned_3motifs, tuned_rew_3motifs)

# rlc_rew, errs_rew = rel_counts_from_data(aniso_rew_2motifs, aniso_rew_3motifs)



from matplotlib import rc

matplotlib.rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    
    r'\usepackage[eulergreek]{sansmath}',   
    r'\sansmath',
    r'\usepackage{siunitx}',    
    r'\sisetup{detect-all}',
    r'\usepackage{color}'       
]  

pl.rcParams['xtick.major.pad']=+49.5

fig = pl.figure(facecolor="white")
fig.set_size_inches(7.4,2.25)

# motifs 1-14 drawn on yscale of ax1
# motifs 15-16 drawn on yscale of ax2
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

capsz = 2.
cpt = 1.5
errlw = 1.5
mew = 1.5
lw = 3.
opacity = 0.25
opacity_aniso = 0.6
bwidth = 0.35



def plot_data(rlcs, errs, color, xshift, z_init, opacity=opacity):
    '''
    two bars to create bars with different inner and frame opactiy
    '''

    patch_dict = dict(width=bwidth, linewidth=lw, bottom = 0.)
    fill_dict  = dict(width=bwidth, alpha=opacity, bottom = 0. )
    err_dict   = dict(fmt='none', lw=errlw, capsize=capsz,
                      capthick=cpt, mew = mew)


    # plot valus in the left part of the figure, motifs 1-14
    xs_ax1 = np.array([k-xshift for k in range(1,15)])

    patches_ax1 = ax1.bar(xs_ax1, rlcs[:14],
                          edgecolor=color, facecolor='white',
                          zorder=z_init+1, **patch_dict)

    fill_ax1    = ax1.bar(xs_ax1, rlcs[:14],
                          edgecolor=color, facecolor=color,
                          zorder=z_init+2, **fill_dict)

    _, caps, _  = ax1.errorbar(xs_ax1 + bwidth/2.,
                               rlcs[:14],
                               yerr=errs[:14],
                               zorder=z_init+3, ecolor=color, **err_dict)

    correct_bars(xs_ax1, rlcs[:14]-1, patches_ax1, bwidth)
    correct_bars(xs_ax1, rlcs[:14]-1, fill_ax1, bwidth)


    # plot valus in the right part of the figure, motifs 15-16
    xs_ax2 = np.array([k+1.00-xshift for k in [15,16]])

    patches_ax2 = ax2.bar(xs_ax2, rlcs[14:],
                          edgecolor=color, facecolor='white',
                          zorder=z_init+1, **patch_dict)

    fill_ax2   = ax2.bar(xs_ax2, rlcs[14:],
                              edgecolor=color, facecolor=color,
                              zorder= z_init+2, **fill_dict)

    _, caps, _ = ax2.errorbar(xs_ax2 + bwidth/2.,
                                  rlcs[14:],
                                  yerr=errs[14:],
                                  zorder=z_init+3, ecolor=color, **err_dict)

    correct_bars(xs_ax2, rlcs[14:]-1, patches_ax2, bwidth)
    correct_bars(xs_ax2, rlcs[14:]-1, fill_ax2, bwidth)



plot_data(rlc_aniso, errs_aniso, color['aniso'],
          xshift=0.250, z_init=12,
          opacity=opacity_aniso)

plot_data(rlc_tuned, errs_tuned, color['tuned'],
          xshift=-0.1, z_init=6,
          opacity=opacity_aniso)    



ax1.set_xlim(0.,17+1.25)
ymin, ymax = -1, 3.
yscale = (ymax-ymin)/5.
ax1.set_ylim(ymin, ymax)
ax1.yaxis.set_ticks(range(-1,4,1))

ax2.set_ylim(-6,18) 
# ax2.yaxis.set_ticks(range(0,10,2))



# legend - not currently independent of axis vals
lbl_fntsz = 10
tick_fntsz = 9

xrect=0.9225

ystart=4.685*yscale-1
ydist=0.605*yscale

ax1.add_patch(Rectangle((xrect,ystart), 0.75, 0.2*yscale,
                        facecolor='white', edgecolor=color['aniso'])) 
ax1.add_patch(Rectangle((xrect,ystart), 0.75, 0.2*yscale,
                        facecolor=color['aniso'], edgecolor=color['aniso'],
                        alpha=opacity_aniso)) 
fig.text(0.225,0.85, r'anisotropic', color = 'k',
         fontsize=lbl_fntsz)

ax1.add_patch(Rectangle((xrect,ystart-ydist), 0.75, 0.2*yscale,
                        facecolor='white', edgecolor=color['tuned']))
ax1.add_patch(Rectangle((xrect,ystart-ydist), 0.75, 0.2*yscale,
                        facecolor=color['tuned'], edgecolor=color['tuned'],
                        alpha=opacity_aniso))
fig.text(0.225,0.75, r'tuned anisotropic', color = 'black',
         fontsize=lbl_fntsz)




# axes setup
ax1.spines['bottom'].set_visible(False)
ax1.spines['bottom'].set_position(('data',0))
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('none')
#ax.yaxis.set_ticks_position('left')

ax2.spines['bottom'].set_visible(False)
ax2.spines['bottom'].set_position(('data',1))
ax2.spines['left'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('none')

# substitute broken up x-axis
ax1.axhline(0,0,0.8025, zorder=39, color='k')
ax1.axhline(0,0.855,1., zorder=39, color='k')

# draw dashed separation
ax1.axvline(15.18, 0.025,0.92, color='k',
            linestyle='dashed', linewidth=1.5, dashes=(5, 2.5))


ax1.set_xticks(range(1,18))
ax1.set_xticklabels(['1','2','3',r'\ 4*','5','6','7',
                     '8','9','$\quad$10*','11','$\quad$12*',
                     '13','$\quad$14*','','15','16'])
#    range(1,15)+['',15,16])

ax1.tick_params(axis='both', which='major', labelsize=tick_fntsz)
ax1.set_ylabel(r'$\frac{\text{aniso.~counts}-\text{rewired counts}}' +\
               r'{\text{expected counts}}$',
               size=13)#lbl_fntsz)

for tick_label in ax2.get_yticklabels():
    tick_label.set_fontsize(tick_fntsz)



# make sure that y=1 is aligned
#between ax1 and ax2
align_yaxis(ax1, 0, ax2, 0)

for i in range(1,18):
    draw_motifs(ax1, i, ymin, ymax, ypos= -1.4, highlight=False)


import os
fname = os.path.splitext(os.path.basename(__file__))[0]


pl.savefig('{:s}.pdf'.format(fname), dpi=600, bbox_inches='tight')

