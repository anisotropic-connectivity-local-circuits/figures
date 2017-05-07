
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


def ddcp_Perin(x):
    '''Fitting the curve from Perin 2011'''
    if x==0.:
        return 0.230785669176
    else:
        a = -1.4186123229540666E-03
        b = 2.7630272296832398E-03
        c = -9.4484523305731971E-01
        Offset = 2.3078566917566815E-01
        return  a/(b+pow(x,c)) + Offset


gids = ['0433','513d','9c24','d0b2','f4d7']

bins = np.linspace(0,296*np.sqrt(2),125)
tP = []


for gid in gids:
    tpath = '/home/lab/comp/data/tuned-an-netw' +\
            '_N1000_ed-l296_XY51-{:s}.gt'.format(gid)
    t = gt.load_graph(tpath)
    t_ctrs, t_ps = get_ddcp(t, bins)
    tP.append(t_ps)


pl.clf()
fig = pl.figure()
fig.set_size_inches(2.25,2.25)
#pl.title(r'$\varepsilon ='+'{:.2f}'.format(eps_frac)+'$')
ax = fig.add_subplot(111)

x = t_ctrs
y = np.mean(tP, 0)
error = scipy.stats.sem(tP, 0)
pl.plot(x, y, 'k', color=color['tuned'], label='tuned aniso.')
pl.fill_between(x, y-error, y+error, alpha=0.5, 
                edgecolor=color['tuned'], facecolor=color['tuned'])

xs = np.linspace(0,296*np.sqrt(2),1000)
ys = [ddcp_Perin(x) for x in xs]
pl.plot(xs, ys, color='grey', label='Perin et al.')

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

leg = pl.legend(loc='upper right', frameon=False,
                handlelength=1.8, prop={'size':12})
for legobj in leg.legendHandles:
    legobj.set_linewidth(3.0)


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.png'.format(fname),  dpi=600)
