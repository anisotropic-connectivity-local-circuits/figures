
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl
import numpy as np
import graph_tool as gt

import sys
sys.path.append("..")
from comp.functions import ( get_ddcp )


import pickle, scipy.stats

def plot_ddcp(eps_frac, gid, nbin):
    '''
    plot distance dependent connectivity profile
    '''
    gpath = '/home/lab/comp/data/aniso-netw_N1000' +\
            '_w37.3_ed-l296_4GX7-{:s}.gt'.format(gid)
    g = gt.load_graph(gpath)
    hpath = '/home/lab/comp/data/rew-stat_aniso' +\
            '_rf1.00_ef{:.2f}-{:s}.gt'.format(eps_frac,gid)
    h = gt.load_graph(hpath)

    gcenters, gprobs = get_ddcp(g, nbin)
    hcenters, hprobs = get_ddcp(h, gcenters)
    pl.plot(gcenters, gprobs, label='original')
    pl.plot(hcenters, hprobs, label='rewired')
    

gid = '0bae'
efracs = [0.,0.01,0.02,0.05,0.10,0.15,0.25, 0.5]
#efracs = [0.05]

for eps_frac in efracs:

    fig = pl.figure()
    ax = fig.add_subplot(111)
    plot_ddcp(eps_frac, gid, 150)

    pl.legend()
    
    import os
    fname = os.path.splitext(os.path.basename(__file__))[0]

    pl.savefig('{:s}_ef{:.2f}.png'.format(fname, eps_frac),
               dpi=300,  bbox_inches='tight')
