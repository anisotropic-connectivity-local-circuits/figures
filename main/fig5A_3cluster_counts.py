
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import sys, pickle, itertools
sys.path.append("..")
sys.path.append("../..")

from utils.colors import color

from core.ecounts_process import process_ecounts


dpath = '/home/lab/comp/data/'

with open(dpath+'nmotif_ecounts_aniso_n3_S2500K.p', 'rb') as pfile:
    aniso_data = pickle.load(pfile)

with open(dpath+'nmotif_ecounts_rew_n3_S2500K.p', 'rb') as pfile:
    aniso_rew_data = pickle.load(pfile)

with open(dpath+'nmotif_ecounts_tuned_n3_S2500K.p', 'rb') as pfile:
    tuned_data = pickle.load(pfile)

with open(dpath+'nmotif_ecounts_rew-tuned_n3_S2500K.p', 'rb') as pfile:
    tuned_rew_data = pickle.load(pfile)

    

max_ecount = 6
aniso_means, aniso_SEM = process_ecounts(aniso_data, aniso_rew_data,
                                         max_ecount)
tuned_means, tuned_SEM = process_ecounts(tuned_data, tuned_rew_data,
                                         max_ecount)



matplotlib.rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    
    r'\usepackage[eulergreek]{sansmath}',   
    r'\sansmath',
    r'\usepackage{siunitx}',    
    r'\sisetup{detect-all}'
]  

pl.tick_params(axis='both', which='major', labelsize=11)
pl.rcParams['xtick.major.pad']=+25


fig = pl.figure(facecolor="white")
fig.set_size_inches(6.46, 2.8*0.9)

ax = fig.add_subplot(111)

xmin, xmax = 0, max_ecount+1
ymin, ymax = -0.5,4.1


ax.set_ylim(ymin,ymax)
ax.set_yticks([0,1,2,3,4])

ax.set_xticks([i+0.55 for i in range(0,xmax,2)])
ax.set_xticklabels([str(i) for i in range(0,xmax,2)])
ax.set_xlim(xmin,xmax)

ax.set_ylabel(r'\LARGE$\frac{\mathrm{counts} - \mathrm{rewired}' +\
               '\,\, \mathrm{counts}}{\mathrm{rewired}' +\
               '\,\,\mathrm{counts}}$', labelpad=8.)



opacity = 0.6
lw = 2.5


aniso_patches = ax.bar([i+0.15+0.225 for i in range(xmax)], aniso_means,
                       width=0.6, edgecolor=color['aniso'],
                       facecolor='white', linewidth=lw, zorder=1)

aniso_fill = ax.bar([i+0.15+0.225 for i in range(xmax)], aniso_means,
                    width=0.6, edgecolor=color['aniso'], 
                    color=color['aniso'], alpha=opacity, zorder=2)

_, caplines, _ = ax.errorbar([i+0.15+0.225+0.3 for i in range(xmax)],
                             aniso_means, fmt='none', yerr=aniso_SEM,
                             ecolor=color['aniso'], lw=1.5, capsize=2.75,
                             mew = 1.5, zorder=3)


tuned_patches = ax.bar([i+0.15 for i in range(xmax)], tuned_means,
                       width=0.6, edgecolor=color['tuned'],
                       facecolor='white', linewidth=lw, zorder=5)

tuned_fill = ax.bar([i+0.15 for i in range(xmax)], tuned_means,
                    width=0.6, edgecolor=color['tuned'],
                    facecolor=color['tuned'], alpha = opacity, zorder = 6)

ax.errorbar([i+0.15+0.3 for i in range(xmax)], tuned_means,
            fmt='none', yerr=tuned_SEM, ecolor=color['tuned'],
            lw=1.5, capsize=2.75, mew = 1.5, zorder=7)


for capline in caplines:
    capline.set_zorder(4)

ax.spines['bottom'].set_zorder(10)


clip_boxes = [pl.Rectangle([x+0.15+0.225,0], 0.6, y,) \
              for x,y in zip(range(xmax),aniso_means)]

for clip_box,bar in zip(clip_boxes,aniso_patches):
    bar.set_clip_path(clip_box.get_path(), bar.get_transform())
    
for clip_box,bar in zip(clip_boxes,aniso_fill):
    bar.set_clip_path(clip_box.get_path(), bar.get_transform())

clip_boxes = [pl.Rectangle([x+0.15,0], 0.6, y,) \
              for x,y in zip(range(xmax),tuned_means)]

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

fig.text(0.2, 0.74, r'3 neuron cluster', size=13)

ax.add_patch(Rectangle((xrect,yrect1), rect_len, rect_w, lw=1.25,
                       edgecolor=color['tuned'], facecolor='white')) 
ax.add_patch(Rectangle((xrect,yrect1), rect_len, rect_w, alpha=opacity,
                       edgecolor=color['tuned'], facecolor=color['tuned']))
fig.text(0.275,0.62, r'tuned anisotropic', color = 'black', fontsize=13) 

ax.add_patch(Rectangle((xrect,yrect2), rect_len, rect_w, lw=1.25,
                       facecolor='white', edgecolor=color['aniso']))
ax.add_patch(Rectangle((xrect,yrect2), rect_len, rect_w, alpha=opacity,
                       facecolor = color['aniso'], edgecolor=color['aniso']))
fig.text(0.275,0.52, r'anisotropic', color = 'black', fontsize=13)


ax.spines['bottom'].set_position(('data',0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('left')


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.pdf'.format(fname), dpi=600, bbox_inches='tight')
