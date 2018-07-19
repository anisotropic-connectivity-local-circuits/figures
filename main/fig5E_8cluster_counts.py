
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import sys, pickle, itertools
sys.path.append("..")
sys.path.append("../..")

import numpy as np

from utils.colors import color

from core.ecounts_process import process_ecounts


dpath = '/home/lab/comp/data/'
#dpath = '/home/fh/sci/lab/aniso_netw/ploscb_18/comp/data/'

with open(dpath+'nmotif_ecounts_aniso_n8_S2500K.p', 'rb') as pfile:
    aniso_data = pickle.load(pfile)

with open(dpath+'nmotif_ecounts_rew_n8_S2500K.p', 'rb') as pfile:
    aniso_rew_data = pickle.load(pfile)

with open(dpath+'nmotif_ecounts_tuned_n8_S2500K.p', 'rb') as pfile:
    tuned_data = pickle.load(pfile)

with open(dpath+'nmotif_ecounts_rew-tuned_n8_S2500K.p', 'rb') as pfile:
    tuned_rew_data = pickle.load(pfile)

    

max_ecount = 22
aniso_means, aniso_SEM = process_ecounts(aniso_data, 
                                         aniso_rew_data, max_ecount)
tuned_means, tuned_SEM = process_ecounts(tuned_data, 
                                           tuned_rew_data, max_ecount)


ymin, ymax = -0.5,4.1
xmin, xmax = 0, max_ecount+1


from matplotlib import rc
rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
       r'\usepackage{siunitx}',   # micro symbols
       r'\sisetup{detect-all}',   # force siunitx to actually use the fonts
       r'\usepackage{tgheros}',    # normal font here
       r'\usepackage{sansmath}',  # sansmath to match helvet
       r'\sansmath'               # actually tell tex to use it!
]  



pl.tick_params(axis='both', which='major', labelsize=11)
pl.rcParams['xtick.major.pad']=+27.5

fig = pl.figure(facecolor="white")
ax = fig.add_subplot(111)

ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('left')

ax.set_ylim(ymin,ymax)
ax.set_yticks([0,1,2,3,4])


ax.set_ylabel(r'\LARGE$\frac{\mathrm{counts} - \mathrm{rewired}\,\, \mathrm{counts}}{\mathrm{rewired}\,\,\mathrm{counts}}$', labelpad=8.)


xlength = max_ecount+1
ax.set_xticks([i+0.5 for i in range(0,xlength,1)], [str(i) for i in range(0,xlength,1)])
ax.set_xlim(xmin,xmax)

# ax.bar([i+0.15+0.225 for i in range(xlength)], aniso_means, width=0.6, yerr = aniso_SEM, edgecolor=color['aniso'], color = color['aniso'], error_kw=dict(ecolor='k', lw=1.5, capsize=3., capthick=10, mew = 1.5))

# ax.bar([i+0.15 for i in range(xlength)], tuned_means, width = 0.6, yerr=tuned_SEM, edgecolor=color['tuned'], color = color['tuned'], error_kw=dict(ecolor='k', lw=1.5, capsize=3., capthick=10, mew = 1.5))


# for opacity bars
opacity = 0.6
lw = 2.5

# for testing!
#ax.bar([i+0.15+0.225 for i in range(xlength)], aniso_means, width = 0.6, edgecolor='k', facecolor='white', zorder = 1)

aniso_patches = ax.bar([i+0.15+0.225 for i in range(xlength)], aniso_means, width=0.6, edgecolor=color['aniso'], facecolor = 'white', linewidth = lw, zorder = 1 )

aniso_fill = ax.bar([i+0.15+0.225 for i in range(xlength)], aniso_means, width=0.6, edgecolor=color['aniso'], color = color['aniso'], alpha = opacity, zorder = 2)

_, caplines, _ = ax.errorbar([i+0.15+0.225+0.3 for i in range(xlength)], aniso_means, fmt='none', yerr = aniso_SEM, ecolor=color['aniso'], lw=1.5, capsize=4., mew = 1.5, zorder=3)

# for testing!
#ax.bar([i+0.15 for i in range(xlength)], tuned_means, width = 0.6, edgecolor='k', facecolor='white', zorder = 4)

tuned_patches = ax.bar([i+0.15 for i in range(xlength)], tuned_means, width = 0.6, edgecolor=color['tuned'], facecolor = 'white', linewidth=lw, zorder=5)

tuned_fill = ax.bar([i+0.15 for i in range(xlength)], tuned_means, width = 0.6, edgecolor=color['tuned'], facecolor = color['tuned'], alpha = opacity, zorder = 6)

ax.errorbar([i+0.15+0.3 for i in range(xlength)], tuned_means, fmt='none', yerr = tuned_SEM, ecolor=color['tuned'], lw=1.5, capsize=4., mew = 1.5, zorder=7)

for capline in caplines:
    capline.set_zorder(4)

ax.spines['bottom'].set_zorder(10)

clip_boxes = [pl.Rectangle([x+0.15+0.225,0], 0.6, y,) for x,y in zip(range(xlength),aniso_means)]

for clip_box,bar in zip(clip_boxes,aniso_patches):
    bar.set_clip_path(clip_box.get_path(), bar.get_transform())
    
for clip_box,bar in zip(clip_boxes,aniso_fill):
    bar.set_clip_path(clip_box.get_path(), bar.get_transform())

clip_boxes = [pl.Rectangle([x+0.15,0], 0.6, y,) for x,y in zip(range(xlength),tuned_means)]

for clip_box,bar in zip(clip_boxes,tuned_patches):
    bar.set_clip_path(clip_box.get_path(), bar.get_transform())
    
for clip_box,bar in zip(clip_boxes,tuned_fill):
    bar.set_clip_path(clip_box.get_path(), bar.get_transform())



xscale = 23
yscale = 4.5

xrect = (1.425-0.15)/xscale*(xmax-xmin) +0.15
yrect1 =  (1.89+3.445-2.875)/yscale*(ymax-ymin) #3.445/yscale*(ymax-ymin)
yrect2 =  1.89/yscale*(ymax-ymin)              #2.875/yscale*(ymax-ymin)
rect_len = 2./xscale*(xmax-xmin)
rect_w = 0.2/yscale*(ymax-ymin)

xtext = 0.275/xscale*(xmax-xmin)
ytext1 = 0.8/yscale*(ymax-ymin)
ytext2 = 0.7/yscale*(ymax-ymin)

from matplotlib.patches import Rectangle

fig.text(0.2, 0.74, r'\textbf{3 neuron cluster}', color = 'black', fontsize=13)

ax.add_patch(Rectangle((xrect,yrect1), rect_len, rect_w, edgecolor = color['tuned'], facecolor='white', lw=1.25)) 
ax.add_patch(Rectangle((xrect,yrect1), rect_len, rect_w, edgecolor = color['tuned'], facecolor=color['tuned'], alpha=opacity))
fig.text(0.275,0.62, r'tuned anisotropic', color = 'black', fontsize=13) 

ax.add_patch(Rectangle((xrect,yrect2), rect_len, rect_w, facecolor = 'white', edgecolor=color['aniso'], lw=1.25))
ax.add_patch(Rectangle((xrect,yrect2), rect_len, rect_w, facecolor = color['aniso'], edgecolor=color['aniso'], alpha=opacity))
fig.text(0.275,0.52, r'anisotropic', color = 'black', fontsize=13)



xfigsize = 6.46
yfigsize = 2.8*0.9
fig.set_size_inches(xfigsize, yfigsize)


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.png'.format(fname), dpi=600)
