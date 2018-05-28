
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
    rew_2motifs = pickle.load(pfile)

fpath = '/home/lab/comp/data/two_motif_counts_dist.p'
with open(fpath, 'rb') as pfile:
    dist_2motifs = pickle.load(pfile)


fpath = '/home/lab/comp/data/three_motif_counts_aniso_S300000.p'
with open(fpath, 'rb') as pfile:
    aniso_3motifs = pickle.load(pfile)

fpath = '/home/lab/comp/data/three_motif_counts_rew_S300000.p'
with open(fpath, 'rb') as pfile:
    rew_3motifs = pickle.load(pfile)

fpath = '/home/lab/comp/data/three_motif_counts_dist_S300000.p'
with open(fpath, 'rb') as pfile:
    dist_3motifs = pickle.load(pfile)

    

def rel_counts_from_data(net_2motifs, net_3motifs):
    '''
    get the occurrence of three motifs relative to
    expected three motifs from two motif occurrence
    '''
    net_2motif_p = motif_count_dict_to_p_array(net_2motifs)
    
    exp_3motif_p = []
    for up,sp,rp in net_2motif_p:
        p_3motif = expected_3motif_p_from_2motif_p(up, sp, rp)
        exp_3motif_p.append(p_3motif)
        
    net_3motif_p = motif_count_dict_to_p_array(net_3motifs)

    rel_counts = net_3motif_p/np.array(exp_3motif_p)

    return np.mean(rel_counts,axis=0), stats.sem(rel_counts, axis=0)
                   

rlc_aniso, errs_aniso = rel_counts_from_data(aniso_2motifs, aniso_3motifs)
rlc_rew, errs_rew = rel_counts_from_data(rew_2motifs, rew_3motifs)
rlc_dist, errs_dist = rel_counts_from_data(dist_2motifs, dist_3motifs)



from matplotlib import rc
 
rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    # helvetica font
    r'\usepackage{sansmath}',   # math-font matching  helvetica
    r'\sansmath'                # actually tell tex to use it!
    r'\usepackage{siunitx}',    # micro symbols
    r'\sisetup{detect-all}',    # force siunitx to use the fonts
]  

pl.rcParams['xtick.major.pad']=+45

fig = pl.figure(facecolor="white")
fig.set_size_inches(7.2,2.25)

# motifs 1-14 drawn on yscale of ax1
# motifs 15-16 drawn on yscale of ax2
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

capsz = 3.25
cpt = 1.5
errlw = 1.5
mew = 1.5
lw = 3.
opacity = 0.25
opacity_aniso = 0.6
bwidth = 0.5

patch_dict = dict(width=bwidth, linewidth=lw, bottom = 1.)
fill_dict  = dict(width=bwidth, alpha=opacity, bottom = 1. )
err_dict   = dict(fmt='none', lw=errlw, capsize=capsz,
                  capthick=cpt, mew = mew)

# # Motifs 15 and 16 get divided by 2 to bring them on 5 scale size
# plot_vals_dist = (p_mean_dist/ps)-1
# plot_vals_dist[-1] = plot_vals_dist[-1]/2.
# plot_vals_dist[-2] = plot_vals_dist[-2]/2.

# p_err_vals_dist = p_err_dist/ps
# p_err_vals_dist[-1] = p_err_vals_dist[-1]/2.
# p_err_vals_dist[-2] = p_err_vals_dist[-2]/2.

# # hatch='///////'

xs_dist_ax1 = np.array([k-0.00 for k in range(1,15)])

dist_patches_ax1 = ax1.bar(xs_dist_ax1, rlc_dist[:14]-1,
                           edgecolor=color['dist'], facecolor='white',
                           zorder=1, **patch_dict)

dist_fill_ax1   = ax1.bar(xs_dist_ax1, rlc_dist[:14]-1,
                          edgecolor=color['dist'], facecolor=color['dist'],
                          zorder = 2, **fill_dict)

_, caplines, _ = ax1.errorbar(xs_dist_ax1 + bwidth/2.,
                              rlc_dist[:14],
                              yerr = errs_dist[:14],
                              zorder = 3, ecolor=color['dist'], **err_dict)

for capline in caplines:
    capline.set_zorder(3)


# # Motifs 15 and 16 get divided by 2 to bring them on 5 scale size
# plot_vals_rew = (p_mean_rew/ps)-1
# plot_vals_rew[-1] = plot_vals_rew[-1]/2.
# plot_vals_rew[-2] = plot_vals_rew[-2]/2.

# p_err_vals_rew = p_err_rew/ps
# p_err_vals_rew[-1] = p_err_vals_rew[-1]/2.
# p_err_vals_rew[-2] = p_err_vals_rew[-2]/2.

# xs_rew = np.array([k-0.125 for k in range(1,len(p_mean)+1)])

# rew_patches = ax.bar(xs_rew, plot_vals_rew, bwidth, linewidth=lw, bottom = 1., edgecolor=color['rew'], facecolor = 'white', zorder=4)

# rew_fill = ax.bar(xs_rew, plot_vals_rew, bwidth, bottom = 1., edgecolor=color['rew'], facecolor = color['rew'], alpha = opacity, zorder=5)

# _, caplines, _ = ax.errorbar(xs_rew + bwidth/2., plot_vals_rew+1, fmt='none', yerr = p_err_vals_rew, lw=errlw, capsize=capsz, capthick=cpt, mew = mew, zorder = 6, ecolor = color['rew'])

# for capline in caplines:
#     capline.set_zorder(6)


# # Motifs 15 and 16 get divided by 2 to bring them on 5 scale size
# #plot_vals = (p_mean/ps)-1
# print("Using temp")
# plot_vals = np.mean(ld, axis=0) -1

# # for j,val in enumerate(plot_vals):
# #     print j+1, "%.2f" %val

# # print "\n"

# plot_vals[-1] = plot_vals[-1]/2.
# plot_vals[-2] = plot_vals[-2]/2.

# #p_err_vals = p_err/ps
# print("Using error temp")
# p_err_vals = stats.sem(ld, axis=0)
# p_err_vals[-1] = p_err_vals[-1]/2.
# p_err_vals[-2] = p_err_vals[-2]/2.

# # for j,val in enumerate(plot_vals):
# #     print j+1, "%.2f" %val

# xs_aniso = np.array([k-0.250 for k in range(1,len(p_mean)+1)])

# aniso_patches = ax.bar(xs_aniso, plot_vals, bwidth, bottom = 1., edgecolor = color['aniso'], facecolor = 'white', linewidth=lw, zorder=7)

# aniso_fill = ax.bar(xs_aniso, plot_vals, bwidth, bottom = 1., edgecolor = color['aniso'], facecolor = color['aniso'], alpha=opacity_aniso, zorder=8)

# _, caplines, _ = ax.errorbar(xs_aniso+bwidth/2., plot_vals+1, fmt='none', yerr = p_err_vals, lw=errlw, capsize=capsz, capthick=cpt, mew = mew, zorder = 9, ecolor = color['aniso'])

# for capline in caplines:
#     capline.set_zorder(9)

# def correct_bar_sizes(xs, ys, patches):

#     clip_boxes = [pl.Rectangle([x,0], bwidth, y,) for x,y in zip(xs,ys)]

#     for clip_box,bar in zip(clip_boxes,patches):
#         bar.set_clip_path(clip_box.get_path(), bar.get_transform())


# correct_bar_sizes(xs_aniso, plot_vals, aniso_patches)
# correct_bar_sizes(xs_aniso, plot_vals, aniso_fill)

# correct_bar_sizes(xs_rew, plot_vals_rew, rew_patches)
# correct_bar_sizes(xs_rew, plot_vals_rew, rew_fill)

correct_bars(xs_dist_ax1, rlc_aniso[:14]-1, dist_patches_ax1, bwidth)
correct_bars(xs_dist_ax1, rlc_aniso[:14]-1, dist_fill_ax1, bwidth)

lbl_fntsz = 10
tick_fntsz = 9


xrect=0.9225
ystart=4.655
ydist=0.745

ax1.add_patch(Rectangle((xrect,ystart), 0.75, 0.2, facecolor = 'white', edgecolor = color['aniso'])) 
ax1.add_patch(Rectangle((xrect,ystart), 0.75, 0.2, facecolor = color['aniso'], edgecolor = color['aniso'], alpha=opacity_aniso)) 
fig.text(0.225,0.85, r'anisotropic', color = 'k', fontsize=lbl_fntsz)

ax1.add_patch(Rectangle((xrect,ystart-ydist), 0.75, 0.2, facecolor = 'white', edgecolor=color['rew']))
ax1.add_patch(Rectangle((xrect,ystart-ydist), 0.75, 0.2, facecolor = color['rew'], edgecolor=color['rew'], alpha=opacity))
fig.text(0.225,0.75, r'rewired', color = 'black', fontsize=lbl_fntsz)

ax1.add_patch(Rectangle((xrect,ystart-2*ydist), 0.75, 0.2, facecolor = 'white', edgecolor=color['dist']))
ax1.add_patch(Rectangle((xrect,ystart-2*ydist), 0.75, 0.2, facecolor = color['dist'], edgecolor=color['dist'], alpha=opacity))
fig.text(0.225,0.65, r'distance-dependent', color = 'black', fontsize=lbl_fntsz)


#pl.savefig(path, dpi=params.dpi, bbox_inches='tight')

# for i in range(13):
#     draw_motifs(i, ymin, ymax, highlight=True)




## Testing the double axis set-up
## Motifs 15 and 16 get divided by 6 to bring them on 5 scale size
#plot_vals = (p_mean/ps)-1

#ax2.bar([k-0.350 for k in range(1,len(p_mean)+1)], plot_vals, 0.5, bottom = 1., edgecolor = 'g', facecolor = 'g', yerr = p_err/ps, error_kw=dict(ecolor='red', lw=1.5, capsize=5, capthick=10, mew = 1.5))


pl.xticks(range(1,18), range(1,15)+['',15,16])
#ax.xaxis.set_ticks(range(1,14),[str(i) for i in range(4,17)])


ax1.spines['bottom'].set_visible(False)
ax2.spines['bottom'].set_visible(False)

ax1.axhline(1,0,0.785, zorder=39, color='k')
ax1.axhline(1,0.86,1., zorder=39, color='k')


ax1.tick_params(axis='both', which='major', labelsize=tick_fntsz)

ax1.set_xlim(0.,17+1.25)

ax1.spines['bottom'].set_position(('data',1))
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.xaxis.set_ticks_position('none')
#ax.yaxis.set_ticks_position('left')

ax1.set_ylabel('relative counts', size=lbl_fntsz)


for tick_label in ax2.get_yticklabels():
    tick_label.set_fontsize(tick_fntsz)

ax2.set_ylim(top=9) #!!



ymin = 0
ymax = 5
ax1.set_ylim(ymin, ymax)

ax2.yaxis.set_ticks(range(0,10,2))

ax2.spines['bottom'].set_position(('data',1))
ax2.spines['left'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('none')

align_yaxis(ax1, 1, ax2, 1)

for i in range(1,18):
    draw_motifs(ax1, i, ymin, ymax, highlight=False)


path='fig4_three_motifs.png'
fig.savefig(path, dpi=300, bbox_inches='tight')

#fig.savefig("/users/hoffmann/Downloads/"+label+params.extension, dpi=params.dpi, bbox_inches='tight')

pl.close('all')
