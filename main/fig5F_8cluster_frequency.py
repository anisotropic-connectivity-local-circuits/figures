

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import sys, pickle, itertools
sys.path.append("..")
sys.path.append("../..")

import numpy as np
from scipy import stats

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
    



def dict_to_array(int_dict, list_length):    
    out_array = np.zeros(list_length)
    for i in range(list_length):
        out_array[i] = int_dict[i]
    return out_array


def process_8counts(data, max_ecount):

    org_array = np.zeros((len(data), max_ecount+1))

    for gid,ecounts in data.iteritems():
        org_array[int(gid),:] += dict_to_array(ecounts, max_ecount+1)

    ecounts_mu = np.mean(org_array, axis = 0)
    ecounts_sem =  stats.sem(org_array, axis = 0, ddof = 0)
        
    return ecounts_mu, ecounts_sem


   


max_count = 23


aniso_means, aniso_SEM = process_8counts(aniso_data, max_count)

aniso_rew_means, aniso_rew_SEM = process_8counts(aniso_rew_data, max_count)

# aniso_dist_means, aniso_dist_SEM = process_8counts(perin_compare_dist_data, max_count)

tanfit_means, tanfit_SEM = process_8counts(tuned_data, max_count)

tanfit_rew_means, tanfit_rew_SEM = process_8counts(tuned_rew_data, max_count)



from matplotlib import rc
rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
       r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
       r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
       r'\usepackage{helvet}',    # set the normal font here
       r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
       r'\sansmath'               # <- tricky! -- gotta actually tell tex to use!
]



fig = pl.figure(facecolor="white")
ax = fig.add_subplot(111)

pl.tick_params(axis='both', which='major', labelsize=14)

x = range(len(aniso_means))

ax.errorbar(x, tanfit_rew_means, color='k', yerr=tanfit_rew_SEM, label="rewired")
ax.errorbar(x, tanfit_means, color=color['tuned'], yerr=tanfit_SEM, label="anisotropic")

# ax.errorbar(x, aniso_rew_means, color=col.rew, yerr=aniso_rew_SEM)
# ax.errorbar(x, aniso_means, color=col.aniso, yerr=aniso_SEM)

#ax.errorbar(x, tanfit_dist_means, color=col.dist, yerr=tanfit_dist_SEM)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

pl.xlabel('connections in clusters of 8 Cells', labelpad=18, size=15)
ax.xaxis.set_label_coords(0.4, -0.2105)
pl.ylabel('frequency', size=15)


handles, labels = ax.get_legend_handles_labels()
handles = [h[0] for h in handles]
pl.legend(handles[::-1], labels[::-1], loc='lower left', frameon=False, fontsize=15)

ax.set_xlim(0,max_count-0.5)


ax.set_yscale('log')
# a = pl.gca()
# a.set_xticklabels([str(int(tck)) for tck in a.get_xticks()], fontProperties)
# a.set_yticklabels(["$10^{-5}$","$10^{-5}$", "$10^{-5}$", "$10^{-5}$", "$10^{-5}$"], fontProperties)

# print a.get_xticks()
# print a.get_yticks()


#fig.set_size_inches(params.xfigsize,params.yfigsize)


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

pl.savefig('{:s}.png'.format(fname), dpi=600, bbox_inches='tight')


# pl.savefig("/home/fh/load/frequency_try_tanfit.pdf", dpi=params.dpi, bbox_inches='tight', pad_inches=0.125)
# pl.close('all')









#
