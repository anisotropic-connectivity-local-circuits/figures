
import sys, pickle, itertools
sys.path.append("..")
sys.path.append("../../")
sys.path.append("../../comp/functions/")

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import graph_tool as gt

import numpy as np
from scipy import stats

from network_eval import get_common_neighbours

from utils.colors import color



def extract(nb, bins):

    counts, bins = np.histogram(nb, bins)

    # occ = np.zeros(1000)
    # nb = np.array(nb)
    
    # for k in range(1000):
    #     occ[k] += np.sum(nb==k)

    # print(occ)

    return counts, bins



ngraphs, binw = 5,1

bins = np.arange(0,1000+binw,binw)
centers = 0.5*(bins[1:]+bins[:-1])

in_aniso  = np.zeros((ngraphs, len(bins)-1))
in_r025    = np.zeros((ngraphs, len(bins)-1))
in_rew    = np.zeros((ngraphs, len(bins)-1))

in_dist   = np.zeros((ngraphs, len(bins)-1))
in_r025dist  = np.zeros((ngraphs, len(bins)-1))
in_rdist  = np.zeros((ngraphs, len(bins)-1))

in_tuned  = np.zeros((ngraphs, len(bins)-1))
in_r025tuned  = np.zeros((ngraphs, len(bins)-1))
in_rtuned  = np.zeros((ngraphs, len(bins)-1))

in_r10    = np.zeros((ngraphs, len(bins)-1))

# out_aniso  = np.zeros((ngraphs, len(bins)-1))
# out_rew    = np.zeros((ngraphs, len(bins)-1))
# out_dist   = np.zeros((ngraphs, len(bins)-1))
# out_rdist  = np.zeros((ngraphs, len(bins)-1))
# out_tuned  = np.zeros((ngraphs, len(bins)-1))
# out_rtuned = np.zeros((ngraphs, len(bins)-1))


for gid in range(ngraphs):
    pass

    gpath = '/home/lab/comp/data/aniso-netw_N1000' +\
            '_w37.3_ed-l296_4GX7-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_aniso[gid,:]+=extract(in_nb, bins)[0]/10.**3

    gpath = '/home/lab/comp/data/rew_aniso_netw_rfrac0.25' +\
            '_efrac0.05-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_r025[gid,:]+=extract(in_nb, bins)[0]/10.**3

    gpath = '/home/lab/comp/data/rew-netw_rfrac1.00' +\
            '_efrac0.05_4FU2-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_rew[gid,:]+=extract(in_nb, bins)[0]/10.**3

    
    gpath = '/home/lab/comp/data/dist-an-netw_N1000_w37.3' +\
            '_ed-l296_8CY2-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_dist[gid,:]+=extract(in_nb, bins)[0]/10.**3

    gpath = '/home/lab/comp/data/rew_dist_netw_rfrac0.25' +\
            '_efrac0.05-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_r025dist[gid,:]+=extract(in_nb, bins)[0]/10.**3
    
    gpath = '/home/lab/comp/data/rew_dist_netw_rfrac1.00' +\
            '_efrac0.05-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_rdist[gid,:]+=extract(in_nb, bins)[0]/10.**3

    
    gpath = '/home/lab/comp/data/tuned-an-netw_N1000' +\
            '_ed-l296_XY51-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_tuned[gid,:]+=extract(in_nb, bins)[0]/10.**3
    
    gpath = '/home/lab/comp/data/rew_tuned_netw' +\
            '_rfrac0.25_efrac0.05-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_r025tuned[gid,:]+=extract(in_nb, bins)[0]/10.**3

    gpath = '/home/lab/comp/data/rew_tuned_netw' +\
            '_rfrac1.00_efrac0.05-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_rtuned[gid,:]+=extract(in_nb, bins)[0]/10.**3

    
    # gpath = '/home/lab/comp/data/rew-netw-repeat_rfrac1.00' +\
    #         '_efrac{:.2f}_4FU2_r10-{:02d}.gt'.format(0.05,gid)
    # g = gt.load_graph(gpath)
    # pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    # in_r10[gid,:]+=extract(in_nb, bins)[0]
    # out_r10[gid,:]+=extract(out_nb, bins)[0]



    
matplotlib.rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    
    r'\usepackage[eulergreek]{sansmath}',   
    r'\sansmath',
    r'\usepackage{siunitx}',    
    r'\sisetup{detect-all}',
    r'\usepackage{color}'
]  





fig, axs = pl.subplots(nrows=1, ncols=3)
ax1, ax2, ax3 = axs
fig.set_size_inches(12.4,2.25)


ax1.errorbar(centers, np.mean(in_aniso, axis=0),
             yerr=stats.sem(in_aniso,axis=0), capsize=0,
             color=color['aniso'])
ax1.errorbar(centers, np.mean(in_r025, axis=0),
             yerr=stats.sem(in_r025,axis=0), capsize=0,
             color=color['rew'], linestyle='dashed')
ax1.errorbar(centers, np.mean(in_rew, axis=0),
             yerr=stats.sem(in_rew,axis=0), capsize=0,
             color=color['rew'])


ax2.errorbar(centers, np.mean(in_rdist, axis=0),
             yerr=stats.sem(in_rdist,axis=0), capsize=0,
             color='black')
ax2.errorbar(centers, np.mean(in_r025dist, axis=0),
             yerr=stats.sem(in_r025dist,axis=0), capsize=0,
             color='black', linestyle='dashed')
ax2.errorbar(centers, np.mean(in_dist, axis=0),
             yerr=stats.sem(in_dist,axis=0), capsize=0,
             color=color['dist'])


ax3.errorbar(centers, np.mean(in_tuned, axis=0),
             yerr=stats.sem(in_tuned,axis=0), capsize=0,
             color=color['tuned'])
ax3.errorbar(centers, np.mean(in_r025tuned, axis=0),
             yerr=stats.sem(in_r025tuned,axis=0), capsize=0,
             color='black', linestyle='dashed')
ax3.errorbar(centers, np.mean(in_rtuned, axis=0),
             yerr=stats.sem(in_rtuned,axis=0), capsize=0,
             color='black')



# ax.errorbar(centers, np.mean(in_r10, axis=0),
#             yerr=stats.sem(in_r10,axis=0), capsize=0)



ax1.set_ylabel('occurrence $10^3$')

for ax in axs:

    ax.set_xlim(0,75)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    ax.set_xlabel('number of common inputs')


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.pdf'.format(fname), dpi=600, bbox_inches='tight')
