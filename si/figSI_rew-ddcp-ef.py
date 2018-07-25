
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import numpy as np
import graph_tool as gt

import sys
sys.path.append("..")
sys.path.append("../..")
from comp.functions import ( get_ddcp )
from utils.colors import color

import pickle, scipy.stats

from matplotlib import rc
rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    # helvetica font
    r'\usepackage{amsmath}',
    r'\usepackage{bm}',
    r'\usepackage{sansmath}',   # math-font matching helvetica
    r'\sansmath',                # actually tell tex to use it!
    #r'\usepackage{bm}',
    #r'\usepackage{siunitx}',    # micro symbols
    #r'\sisetup{detect-all}'    # force siunitx to use the fonts
    #r'\DeclareSymbolFont{greekletters}{OML}{arev}{m}{it}',
    #r'\DeclareMathSymbol{\varepsilon}{\mathord}{greekletters}{"22}'
]


gids = ['00', '01', '02']
efracs = [0.,0.01,0.02,0.05,0.10,0.15,0.25, 0.5]

for eps_frac in efracs:

    bins = np.linspace(0,296*np.sqrt(2),100)
    gP = []
    hP = []
    
    for gid in gids:
        gpath = '/home/lab/comp/data/aniso-netw_N1000' +\
                '_w37.3_ed-l296_4GX7-{:s}.gt'.format(gid)
        g = gt.load_graph(gpath)
        g_ctrs, g_ps = get_ddcp(g, bins)
        gP.append(g_ps)

        hpath = '/home/lab/comp/data/rew-stat_aniso' +\
                '_rf1.00_ef{:.2f}-{:s}.gt'.format(eps_frac,gid)
        h = gt.load_graph(hpath)
        h_ctrs, h_ps = get_ddcp(h, bins)
        hP.append(h_ps)

    pl.clf()
    fig = pl.figure()
    fig.set_size_inches(2.6*1.2,2.*1.2*0.75)
    pl.title(r'$\bm{\varepsilon} / E ='+'{:.2f}'.format(eps_frac)+'$')
    ax = fig.add_subplot(111)

    x = g_ctrs
    y = np.mean(gP, 0)
    error = scipy.stats.sem(gP, 0)
    pl.plot(x, y, 'k', color=color['aniso'], label='original')
    pl.fill_between(x, y-error, y+error, alpha=0.5, 
                    edgecolor=color['aniso'],
                    facecolor=color['aniso'])

    x = h_ctrs
    y = np.mean(hP, 0)
    error = scipy.stats.sem(hP, 0)
    pl.plot(x, y, 'k', color=color['rew'],  label='rewired')
    pl.fill_between(x, y-error, y+error, alpha=0.5, 
                    edgecolor=color['rew'],
                    facecolor=color['rew'])

    
    leg = pl.legend(frameon=False)
    for legobj in leg.legendHandles:
        legobj.set_linewidth(2.5)
    
    pl.ylim(0,0.525)
    pl.subplots_adjust(left=0.15, right=0.85,
                       top=0.85, bottom=0.15)
    pl.xticks([0,100,200,300,400])

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    import os
    fname = os.path.splitext(os.path.basename(__file__))[0]

    pl.savefig('{:s}{:.2f}.png'.format(fname, eps_frac),
               dpi=600)
