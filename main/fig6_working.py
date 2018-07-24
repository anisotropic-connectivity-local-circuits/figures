
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

    counts, bins = np.histogram(nb, bins, density=True)

    # occ = np.zeros(1000)
    # nb = np.array(nb)
    
    # for k in range(1000):
    #     occ[k] += np.sum(nb==k)

    # print(occ)

    return counts, bins



ngraphs, binw = 5,1

bins = np.arange(0,1000+binw,binw)
centers = 0.5*(bins[1:]+bins[:-1])

in_aniso_all  = np.zeros((ngraphs, len(bins)-1))
in_r025aniso_all  = np.zeros((ngraphs, len(bins)-1))
in_raniso_all  = np.zeros((ngraphs, len(bins)-1))

in_aniso_unc      = np.zeros((ngraphs, len(bins)-1))
in_r025aniso_unc  = np.zeros((ngraphs, len(bins)-1))
in_raniso_unc     = np.zeros((ngraphs, len(bins)-1))

in_aniso_sng      = np.zeros((ngraphs, len(bins)-1))
in_r025aniso_sng  = np.zeros((ngraphs, len(bins)-1))
in_raniso_sng     = np.zeros((ngraphs, len(bins)-1))

in_aniso_bdr      = np.zeros((ngraphs, len(bins)-1))
in_r025aniso_bdr  = np.zeros((ngraphs, len(bins)-1))
in_raniso_bdr     = np.zeros((ngraphs, len(bins)-1))


in_dist_all  = np.zeros((ngraphs, len(bins)-1))
in_r025dist_all  = np.zeros((ngraphs, len(bins)-1))
in_rdist_all  = np.zeros((ngraphs, len(bins)-1))

in_dist_unc      = np.zeros((ngraphs, len(bins)-1))
in_r025dist_unc  = np.zeros((ngraphs, len(bins)-1))
in_rdist_unc     = np.zeros((ngraphs, len(bins)-1))

in_dist_sng      = np.zeros((ngraphs, len(bins)-1))
in_r025dist_sng  = np.zeros((ngraphs, len(bins)-1))
in_rdist_sng     = np.zeros((ngraphs, len(bins)-1))

in_dist_bdr      = np.zeros((ngraphs, len(bins)-1))
in_r025dist_bdr  = np.zeros((ngraphs, len(bins)-1))
in_rdist_bdr     = np.zeros((ngraphs, len(bins)-1))

in_tuned_all  = np.zeros((ngraphs, len(bins)-1))
in_r025tuned_all  = np.zeros((ngraphs, len(bins)-1))
in_rtuned_all  = np.zeros((ngraphs, len(bins)-1))

in_tuned_unc      = np.zeros((ngraphs, len(bins)-1))
in_r025tuned_unc  = np.zeros((ngraphs, len(bins)-1))
in_rtuned_unc     = np.zeros((ngraphs, len(bins)-1))

in_tuned_sng      = np.zeros((ngraphs, len(bins)-1))
in_r025tuned_sng  = np.zeros((ngraphs, len(bins)-1))
in_rtuned_sng     = np.zeros((ngraphs, len(bins)-1))

in_tuned_bdr      = np.zeros((ngraphs, len(bins)-1))
in_r025tuned_bdr  = np.zeros((ngraphs, len(bins)-1))
in_rtuned_bdr     = np.zeros((ngraphs, len(bins)-1))



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
    in_aniso_all[gid,:]+=extract(in_nb       , bins)[0]
    in_aniso_unc[gid,:]+=extract(in_nb[cn==0], bins)[0]
    in_aniso_sng[gid,:]+=extract(in_nb[cn==1], bins)[0]
    in_aniso_bdr[gid,:]+=extract(in_nb[cn==2], bins)[0]

    gpath = '/home/lab/comp/data/rew_aniso_netw_rfrac0.25' +\
            '_efrac0.05-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_r025aniso_all[gid,:]+=extract(in_nb       , bins)[0]
    in_r025aniso_unc[gid,:]+=extract(in_nb[cn==0], bins)[0]
    in_r025aniso_sng[gid,:]+=extract(in_nb[cn==1], bins)[0]
    in_r025aniso_bdr[gid,:]+=extract(in_nb[cn==2], bins)[0]

    gpath = '/home/lab/comp/data/rew-netw_rfrac1.00' +\
            '_efrac0.05_4FU2-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_raniso_all[gid,:]+=extract(in_nb       , bins)[0]
    in_raniso_unc[gid,:]+=extract(in_nb[cn==0], bins)[0]
    in_raniso_sng[gid,:]+=extract(in_nb[cn==1], bins)[0]
    in_raniso_bdr[gid,:]+=extract(in_nb[cn==2], bins)[0]

    
    gpath = '/home/lab/comp/data/dist-an-netw_N1000_w37.3' +\
            '_ed-l296_8CY2-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_dist_all[gid,:]+=extract(in_nb       , bins)[0]
    in_dist_unc[gid,:]+=extract(in_nb[cn==0], bins)[0]
    in_dist_sng[gid,:]+=extract(in_nb[cn==1], bins)[0]
    in_dist_bdr[gid,:]+=extract(in_nb[cn==2], bins)[0]

    gpath = '/home/lab/comp/data/rew_dist_netw_rfrac0.25' +\
            '_efrac0.05-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_r025dist_all[gid,:]+=extract(in_nb       , bins)[0]
    in_r025dist_unc[gid,:]+=extract(in_nb[cn==0], bins)[0]
    in_r025dist_sng[gid,:]+=extract(in_nb[cn==1], bins)[0]
    in_r025dist_bdr[gid,:]+=extract(in_nb[cn==2], bins)[0]
    
    gpath = '/home/lab/comp/data/rew_dist_netw_rfrac1.00' +\
            '_efrac0.05-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_rdist_all[gid,:]+=extract(in_nb       , bins)[0]
    in_rdist_unc[gid,:]+=extract(in_nb[cn==0], bins)[0]
    in_rdist_sng[gid,:]+=extract(in_nb[cn==1], bins)[0]
    in_rdist_bdr[gid,:]+=extract(in_nb[cn==2], bins)[0]

    
    gpath = '/home/lab/comp/data/tuned-an-netw_N1000' +\
            '_ed-l296_XY51-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_tuned_all[gid,:]+=extract(in_nb       , bins)[0]
    in_tuned_unc[gid,:]+=extract(in_nb[cn==0], bins)[0]
    in_tuned_sng[gid,:]+=extract(in_nb[cn==1], bins)[0]
    in_tuned_bdr[gid,:]+=extract(in_nb[cn==2], bins)[0]
    
    gpath = '/home/lab/comp/data/rew_tuned_netw' +\
            '_rfrac0.25_efrac0.05-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_r025tuned_all[gid,:]+=extract(in_nb       , bins)[0]
    in_r025tuned_unc[gid,:]+=extract(in_nb[cn==0], bins)[0]
    in_r025tuned_sng[gid,:]+=extract(in_nb[cn==1], bins)[0]
    in_r025tuned_bdr[gid,:]+=extract(in_nb[cn==2], bins)[0]


    gpath = '/home/lab/comp/data/rew_tuned_netw' +\
            '_rfrac1.00_efrac0.05-{:02d}.gt'.format(gid)
    g = gt.load_graph(gpath)
    pairs, cn, in_nb, out_nb = get_common_neighbours(g)
    in_rtuned_all[gid,:]+=extract(in_nb       , bins)[0]
    in_rtuned_unc[gid,:]+=extract(in_nb[cn==0], bins)[0]
    in_rtuned_sng[gid,:]+=extract(in_nb[cn==1], bins)[0]
    in_rtuned_bdr[gid,:]+=extract(in_nb[cn==2], bins)[0]


    
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





fig, axs = pl.subplots(nrows=4, ncols=3)
fig.set_size_inches(10.4,2.25*4)


axs[0,0].errorbar(centers, np.mean(in_aniso_all, axis=0),
                  yerr=stats.sem(in_aniso_all,axis=0), capsize=0,
                  color=color['aniso'], fmt='-', markersize=0, lw=2, zorder=-0)
axs[0,0].errorbar(centers, np.mean(in_r025aniso_all, axis=0),
                  yerr=stats.sem(in_r025aniso_all,axis=0), capsize=0,
                  color='grey', fmt='-', markersize=0, lw=2, zorder=-1)
axs[0,0].errorbar(centers, np.mean(in_raniso_all, axis=0),
                  yerr=stats.sem(in_raniso_all,axis=0), capsize=0,
                  color=color['rew'], fmt='-', markersize=0, lw=2, zorder=-2)

axs[1,0].errorbar(centers, np.mean(in_aniso_unc, axis=0),
                  yerr=stats.sem(in_aniso_unc,axis=0), capsize=0,
                  color=color['aniso'], fmt='-', markersize=0, lw=2, zorder=-0)
axs[1,0].errorbar(centers, np.mean(in_r025aniso_unc, axis=0),
                  yerr=stats.sem(in_r025aniso_unc,axis=0), capsize=0,
                  color='grey', fmt='-', markersize=0, lw=2, zorder=-1)
axs[1,0].errorbar(centers, np.mean(in_raniso_unc, axis=0),
                  yerr=stats.sem(in_raniso_unc,axis=0), capsize=0,
                  color=color['rew'], fmt='-', markersize=0, lw=2, zorder=-2)

axs[2,0].errorbar(centers, np.mean(in_aniso_sng, axis=0),
                  yerr=stats.sem(in_aniso_sng,axis=0), capsize=0,
                  color=color['aniso'], fmt='-', markersize=0, lw=2, zorder=-0)
axs[2,0].errorbar(centers, np.mean(in_r025aniso_sng, axis=0),
                  yerr=stats.sem(in_r025aniso_sng,axis=0), capsize=0,
                  color='grey', fmt='-', markersize=0, lw=2, zorder=-1)
axs[2,0].errorbar(centers, np.mean(in_raniso_sng, axis=0),
                  yerr=stats.sem(in_raniso_sng,axis=0), capsize=0,
                  color=color['rew'], fmt='-', markersize=0, lw=2, zorder=-2)

axs[3,0].errorbar(centers, np.mean(in_aniso_bdr, axis=0),
                  yerr=stats.sem(in_aniso_bdr,axis=0), capsize=0,
                  color=color['aniso'], fmt='-', markersize=0, lw=2, zorder=-0)
axs[3,0].errorbar(centers, np.mean(in_r025aniso_bdr, axis=0),
                  yerr=stats.sem(in_r025aniso_bdr,axis=0), capsize=0,
                  color='grey', fmt='-', markersize=0, lw=2, zorder=-1)
axs[3,0].errorbar(centers, np.mean(in_raniso_bdr, axis=0),
                  yerr=stats.sem(in_raniso_bdr,axis=0), capsize=0,
                  color=color['rew'], fmt='-', markersize=0, lw=2, zorder=-2)



axs[0,1].errorbar(centers, np.mean(in_dist_all, axis=0),
                  yerr=stats.sem(in_dist_all,axis=0), capsize=0,
                  color=color['dist'], fmt='-', markersize=0, lw=2, zorder=-0)
axs[0,1].errorbar(centers, np.mean(in_r025dist_all, axis=0),
                  yerr=stats.sem(in_r025dist_all,axis=0), capsize=0,
                  color='grey', fmt='-', markersize=0, lw=2, zorder=-1)
axs[0,1].errorbar(centers, np.mean(in_rdist_all, axis=0),
                  yerr=stats.sem(in_rdist_all,axis=0), capsize=0,
                  color='black', fmt='-', markersize=0, lw=2, zorder=-2)

axs[1,1].errorbar(centers, np.mean(in_dist_unc, axis=0),
                  yerr=stats.sem(in_dist_unc,axis=0), capsize=0,
                  color=color['dist'], fmt='-', markersize=0, lw=2, zorder=-0)
axs[1,1].errorbar(centers, np.mean(in_r025dist_unc, axis=0),
                  yerr=stats.sem(in_r025dist_unc,axis=0), capsize=0,
                  color='grey', fmt='-', markersize=0, lw=2, zorder=-1)
axs[1,1].errorbar(centers, np.mean(in_rdist_unc, axis=0),
                  yerr=stats.sem(in_rdist_unc,axis=0), capsize=0,
                  color='black', fmt='-', markersize=0, lw=2, zorder=-2)

axs[2,1].errorbar(centers, np.mean(in_dist_sng, axis=0),
                  yerr=stats.sem(in_dist_sng,axis=0), capsize=0,
                  color=color['dist'], fmt='-', markersize=0, lw=2, zorder=-0)
axs[2,1].errorbar(centers, np.mean(in_r025dist_sng, axis=0),
                  yerr=stats.sem(in_r025dist_sng,axis=0), capsize=0,
                  color='grey', fmt='-', markersize=0, lw=2, zorder=-1)
axs[2,1].errorbar(centers, np.mean(in_rdist_sng, axis=0),
                  yerr=stats.sem(in_rdist_sng,axis=0), capsize=0,
                  color='black', fmt='-', markersize=0, lw=2, zorder=-2)

axs[3,1].errorbar(centers, np.mean(in_dist_bdr, axis=0),
                  yerr=stats.sem(in_dist_bdr,axis=0), capsize=0,
                  color=color['dist'], fmt='-', markersize=0, lw=2, zorder=-0)
axs[3,1].errorbar(centers, np.mean(in_r025dist_bdr, axis=0),
                  yerr=stats.sem(in_r025dist_bdr,axis=0), capsize=0,
                  color='grey', fmt='-', markersize=0, lw=2, zorder=-1)
axs[3,1].errorbar(centers, np.mean(in_rdist_bdr, axis=0),
                  yerr=stats.sem(in_rdist_bdr,axis=0), capsize=0,
                  color='black', fmt='-', markersize=0, lw=2, zorder=-2)



axs[0,2].errorbar(centers, np.mean(in_tuned_all, axis=0),
                  yerr=stats.sem(in_tuned_all,axis=0), capsize=0,
                  color=color['tuned'], fmt='-', markersize=0, lw=2, zorder=-0)
axs[0,2].errorbar(centers, np.mean(in_r025tuned_all, axis=0),
                  yerr=stats.sem(in_r025tuned_all,axis=0), capsize=0,
                  color='grey', fmt='-', markersize=0, lw=2, zorder=-1)
axs[0,2].errorbar(centers, np.mean(in_rtuned_all, axis=0),
                  yerr=stats.sem(in_rtuned_all,axis=0), capsize=0,
                  color='black', fmt='-', markersize=0, lw=2, zorder=-2)

axs[1,2].errorbar(centers, np.mean(in_tuned_unc, axis=0),
                  yerr=stats.sem(in_tuned_unc,axis=0), capsize=0,
                  color=color['tuned'], fmt='-', markersize=0, lw=2, zorder=-0)
axs[1,2].errorbar(centers, np.mean(in_r025tuned_unc, axis=0),
                  yerr=stats.sem(in_r025tuned_unc,axis=0), capsize=0,
                  color='grey', fmt='-', markersize=0, lw=2, zorder=-1)
axs[1,2].errorbar(centers, np.mean(in_rtuned_unc, axis=0),
                  yerr=stats.sem(in_rtuned_unc,axis=0), capsize=0,
                  color='black', fmt='-', markersize=0, lw=2, zorder=-2)

axs[2,2].errorbar(centers, np.mean(in_tuned_sng, axis=0),
                  yerr=stats.sem(in_tuned_sng,axis=0), capsize=0,
                  color=color['tuned'], fmt='-', markersize=0, lw=2, zorder=-0)
axs[2,2].errorbar(centers, np.mean(in_r025tuned_sng, axis=0),
                  yerr=stats.sem(in_r025tuned_sng,axis=0), capsize=0,
                  color='grey', fmt='-', markersize=0, lw=2, zorder=-1)
axs[2,2].errorbar(centers, np.mean(in_rtuned_sng, axis=0),
                  yerr=stats.sem(in_rtuned_sng,axis=0), capsize=0,
                  color='black', fmt='-', markersize=0, lw=2, zorder=-2)

axs[3,2].errorbar(centers, np.mean(in_tuned_bdr, axis=0),
                  yerr=stats.sem(in_tuned_bdr,axis=0), capsize=0,
                  color=color['tuned'], fmt='-', markersize=0, lw=2, zorder=-0)
axs[3,2].errorbar(centers, np.mean(in_r025tuned_bdr, axis=0),
                  yerr=stats.sem(in_r025tuned_bdr,axis=0), capsize=0,
                  color='grey', fmt='-', markersize=0, lw=2, zorder=-1)
axs[3,2].errorbar(centers, np.mean(in_rtuned_bdr, axis=0),
                  yerr=stats.sem(in_rtuned_bdr,axis=0), capsize=0,
                  color='black', fmt='-', markersize=0, lw=2, zorder=-2)



axs[0,0].set_ylabel('relative occurrence')
axs[1,0].set_ylabel('relative occurrence')
axs[2,0].set_ylabel('relative occurrence')
axs[3,0].set_ylabel('relative occurrence')

axs[3,0].set_xlabel('number of common inputs')
axs[3,1].set_xlabel('number of common inputs')
axs[3,2].set_xlabel('number of common inputs')

for ax in axs.reshape(-1):

    ax.set_xlim(0,75)
    ax.set_ylim(bottom=0., top=0.10)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # ax.text(-15, 0.12, r'\textbf{A}', clip_on=False)


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.tight_layout()
pl.savefig('{:s}.pdf'.format(fname), dpi=600, bbox_inches='tight')
