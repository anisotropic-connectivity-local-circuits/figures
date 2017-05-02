
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import numpy as np

import pickle, scipy.stats

from matplotlib import rc
rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    # helvetica font
    r'\usepackage{siunitx}',    # micro symbols
    r'\sisetup{detect-all}'    # force siunitx to use the fonts
    #r'\usepackage[utf8]{inputenc}',
    #r'\usepackage[T1]{fontenc}',
    #r'\usepackage{amsmath, amssymb}',
    r'\usepackage{sansmath}',   # math-font matching helvetica
    r'\sansmath',                # actually tell tex to use it!
    #r'\DeclareSymbolFont{Greekletters}{OT1}{iwona}{m}{n}',
    #r'\DeclareSymbolFont{greekletters}{OML}{arev}{m}{it}',
    #r'\DeclareMathSymbol{\varepsilon}{\mathord}{greekletters}{"22}'
]


def load_data_point(eps_frac, gid):
    dpath = '../comp/data/rew-stat_aniso' +\
            '_rf1.00_ef{:.2f}-{:s}_stat.p'.format(eps_frac,gid)
    with open(dpath, "rb") as pfile:
        rew_stat = pickle.load(pfile)
    return len(rew_stat["fail_edges"])

gids = ['0bae', '1b20', '22df']
efracs = [0.01,0.02,0.05,0.10,0.15,0.25]
nfail_mu = []
nfail_sem = []

for eps_frac in efracs:
    nfails = []
    for gid in gids:
        nfails.append(load_data_point(eps_frac, gid))
    nfail_mu.append(np.mean(nfails))
    nfail_sem.append(scipy.stats.sem(nfails))

fig = pl.figure()    
fig.set_size_inches(2.3*2.25*0.5/0.66,1.9)
ax = fig.add_subplot(111)
pl.errorbar(efracs, nfail_mu, yerr=nfail_sem, linewidth=2.)
pl.ylim(0,1200)
fs = 13.5
pl.xlabel(r'relative rewiring margin $\varepsilon / E$', fontsize=fs)
pl.ylabel('edges not in\n rewired graph', fontsize=fs)
pl.subplots_adjust(left=0.25, right=0.925,
                   top=0.925, bottom=0.30)

pl.yticks(np.linspace(0,1200,5))

import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.png'.format(fname), dpi=600)
