
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import sys, pickle, itertools
sys.path.append("..")
sys.path.append("../..")

import numpy as np
from scipy import stats

from utils.colors import color


dpath = '/home/lab/comp/data/'

with open(dpath+'nmotif_ecounts_dist_n12_S2500K.p', 'rb') as pfile:
    dist_data = pickle.load(pfile)
with open(dpath+'nmotif_ecounts_rew-dist_n12_S2500K.p', 'rb') as pfile:
    dist_rew_data = pickle.load(pfile)
    


def dict_to_array(int_dict, list_length):    
    out_array = np.zeros(list_length)
    for i in range(list_length):
        out_array[i] = int_dict[i]
    return out_array


def process_counts(data, max_ecount):

    org_array = np.zeros((len(data), max_ecount+2))

    for gid,ecounts in data.iteritems():
        org_array[int(gid),:] += dict_to_array(ecounts, max_ecount+2)

    row_sums = org_array.sum(axis=1).astype('float')
    newm = org_array / row_sums[:, np.newaxis]
    
    ecounts_mu = np.mean(newm, axis = 0)
    ecounts_sem =  stats.sem(newm, axis = 0, ddof = 0)
        
    return ecounts_mu, ecounts_sem


   
max_count = 40

dist_means, dist_SEM = process_counts(dist_data, max_count)
dist_rew_means, dist_rew_SEM = process_counts(dist_rew_data, max_count)


matplotlib.rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    
    r'\usepackage[eulergreek]{sansmath}',   
    r'\sansmath',
    r'\usepackage{siunitx}',    
    r'\sisetup{detect-all}'
]  


fig = pl.figure(facecolor="white")
fig.set_size_inches(6.46/2.,2.80*0.935)

ax = fig.add_subplot(111)
ax.tick_params(axis='both', which='major', labelsize=14)


x = range(len(dist_means))
ax.errorbar(x, dist_rew_means, yerr=dist_rew_SEM,
            color='k', label="rewired", capsize=2)
ax.errorbar(x, dist_means, yerr=dist_SEM,
            color=color['dist'], label="dist.~depend.", capsize=2)



ax.set_xlim(0,max_count+0.5)
ax.set_yscale('log')

ax.set_xlabel('connections in clusters of 12 Cells', labelpad=18, size=15)
ax.xaxis.set_label_coords(0.4, -0.2105)
ax.set_ylabel('frequency', size=15)

handles, labels = ax.get_legend_handles_labels()
handles = [h[0] for h in handles]
pl.legend(handles[::-1], labels[::-1], loc='lower left',
          frameon=False, fontsize=15)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.pdf'.format(fname), dpi=600, bbox_inches='tight')
