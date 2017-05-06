
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import numpy as np
import graph_tool as gt

from utils.colors import color

import sys
sys.path.append("..")
from comp.functions import ( get_ddcp )

import pickle, scipy.stats

from matplotlib import rc
rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    # helvetica font
    r'\usepackage{sansmath}',   # math-font matching helvetica
    r'\sansmath'                # actually tell tex to use it!
    r'\usepackage{siunitx}',    # micro symbols
    r'\sisetup{detect-all}'    # force siunitx to use the fonts
]


gids = ['0bae', '1b20', '22df', '8ca5', 'b97d']

bins = np.linspace(0,296*np.sqrt(2),125)
gP = []
hP = []

for gid in gids:
    gpath = '/home/lab/comp/data/aniso-netw_N1000' +\
            '_w37.3_ed-l296_4GX7-{:s}.gt'.format(gid)
    g = gt.load_graph(gpath)
    g_ctrs, g_ps = get_ddcp(g, bins)
    gP.append(g_ps)

    hpath = '/home/lab/comp/data/rew-netw_rfrac1.00' +\
            '_efrac{:.2f}_4FU2-{:s}.gt'.format(0.05,gid)
    h = gt.load_graph(hpath)
    h_ctrs, h_ps = get_ddcp(h, bins)
    hP.append(h_ps)

gids = ['0293', '625f', '696d', 'b6c5', 'd26f']
kP = []

for gid in gids:

    kpath = '/home/lab/comp/data/dist-an-netw_N1000_w37.3' +\
            '_ed-l296_8CY2-{:s}.gt'.format(gid)
    k = gt.load_graph(kpath)
    k_ctrs, k_ps = get_ddcp(k, bins)
    kP.append(k_ps)




pl.clf()
fig = pl.figure()
fig.set_size_inches(2.25,2.25)
#pl.title(r'$\varepsilon ='+'{:.2f}'.format(eps_frac)+'$')
ax = fig.add_subplot(111)

x = g_ctrs
y = np.mean(gP, 0)
error = scipy.stats.sem(gP, 0)
pl.plot(x, y, 'k', color=color['aniso'], label='anisotropic')
pl.fill_between(x, y-error, y+error, alpha=0.5, 
                edgecolor=color['aniso'], facecolor=color['aniso'])

x = g_ctrs
y = np.mean(hP, 0)
error = scipy.stats.sem(hP, 0)
pl.plot(x, y, 'k', color=color['rew'], label='rewired')
pl.fill_between(x, y-error, y+error, alpha=0.5, 
                edgecolor=color['rew'], facecolor=color['rew'])

x = g_ctrs
y = np.mean(kP, 0)
error = scipy.stats.sem(hP, 0)
pl.plot(x, y, 'k', color=color['dist'], label='dist.-dep.')
pl.fill_between(x, y-error, y+error, alpha=0.5, 
                edgecolor=color['dist'], facecolor=color['dist'])


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

ax.set_xlabel('distance')
    
pl.ylim(0,0.55)
pl.xlim(0,400)
pl.subplots_adjust(left=0.15, right=0.94,
                   top=0.875, bottom=0.2)
pl.xticks([0,100,200,300,400])

leg = pl.legend(frameon=False, handlelength=1.8, prop={'size':12})
for legobj in leg.legendHandles:
    legobj.set_linewidth(3.0)


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.png'.format(fname),  dpi=600)
