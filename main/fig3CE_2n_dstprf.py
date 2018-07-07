
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import numpy as np
import scipy.stats as stats
import graph_tool as gt

import sys, math
sys.path.append("..")
sys.path.append("../..")

from utils import color, errorbars_clip_false
from comp.functions import Tuned_netw_dist_profile, get_ddcp

from data.extract_overall_p import xvals_data as Perin2011_x
from data.extract_overall_p import yvals_data as Perin2011_y
from data.extract_overall_p import yerrs_data as Perin2011_yerr


Tuned_netw_dist_profile = Tuned_netw_dist_profile()

xs = np.arange(0,418.6,0.01)
ddcp = np.array([Tuned_netw_dist_profile.ddcp(x) for x in xs])


bins = np.linspace(0,296*np.sqrt(2),8)
tP = []

for gid in range(3):
    tpath = '/home/lab/comp/data/tuned-an-netw' +\
            '_N1000_ed-l296_XY51-{:02d}.gt'.format(gid)
    t = gt.load_graph(tpath)
    t_ctrs, t_ps = get_ddcp(t, bins)
    tP.append(t_ps)

print(np.mean(tP, axis=0))

matplotlib.rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    
    r'\usepackage[eulergreek]{sansmath}',   
    r'\sansmath'                
    r'\usepackage{siunitx}',    
    r'\sisetup{detect-all}',    
]  

fig = pl.figure()
fig.set_size_inches(2.8, 1.95)

ax = fig.add_subplot(111)

ax.plot(xs, ddcp, color='red')
ax.errorbar(Perin2011_x, Perin2011_y, yerr=Perin2011_yerr,
            fmt='.', color='grey')
ax.errorbar(t_ctrs, np.mean(tP, axis=0), yerr=stats.sem(tP, axis=0),
            fmt='.', color=color['tuned'])


ymin, ymax = 0, 0.25
ax.set_ylim(ymin,ymax)
ax.set_xlim(0,418.6)

ax.set_xticks([0,100,200,300,400])

fig.tight_layout()



mew_set = 1.2
msize = 8
ypos = 0.195
awidth = 0.001
hwidth = 0.01
fontsize = 12



#          ?
#    v_1 ----> v_2
#
ax.text(290,ypos-0.002,r'$\mathbf{v_1}$', size=fontsize,
        fontweight='bold', va='center', ha='center', clip_on=False) 
ax.text(374,ypos-0.002,r'$\mathbf{v_2}$', size=fontsize,
        fontweight='bold', va='center', ha='center', clip_on=False)
ax.text(330,ypos+0.02,r'\textbf{?}', size=fontsize,
        fontweight='bold', va='center', ha='center', clip_on=False)
ax.arrow(307.5,ypos, 52-17.5, 0, width=awidth,
         head_width=hwidth, head_length=10, fc='k', ec='k')


#
# custom legend
#
x_in, fontsize = 530, 11
y_start, y_lb, y_pb = 0.2, 0.05, 0.075


errs = ax.errorbar([480,490], [0.2,0.2], yerr=[0.05,0.05],
                   clip_on=False, fmt='.', color=color['tuned'])
errorbars_clip_false(ax,errs)

ax.text(x_in, y_start, 'somatosensory cortex',
        size=fontsize, clip_on=False)
ax.text(x_in, y_start-y_lb, 'from Perin et al.~(2011)',
        size=fontsize, clip_on=False)
ax.text(x_in, y_start-y_lb-y_pb, 'fit to cortex data $p(x)$',
        size=fontsize, clip_on=False)
ax.text(x_in, y_start-y_lb-2*y_pb, 'tuned anisotropic',
        size=fontsize, clip_on=False)




ax.axvline(850, 0, 1, clip_on=False)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

pl.ylabel("connection probability", fontsize=12, labelpad=11.5)
pl.xlabel(r'distance in \SI{}{\micro\meter}', fontsize=12, labelpad=8)

pl.savefig('fig3C_2n_dstprf.png', dpi=300, bbox_inches='tight')

















# #numerical profile

# for data in data_sets:

#     connection_probabilites, bins = data

#     prb_coll= np.dot(0.5,connection_probabilites["prb_single"])+connection_probabilites["prb_recip"]

#     #prb_coll = np.array(connection_probabilites[params.connection_type])

#     probabilites = np.mean(prb_coll, axis = 0)
#     #standard deviation!
#     errors = np.std(prb_coll, axis = 0)

#     #ps = sp*0.5 + rp
#     bin_centers = (bins[:-1]+bins[1:])/2 

#     pl.errorbar(bin_centers, probabilites, markersize = 2.,yerr=errors, fmt = '.',  color='gray', elinewidth = 2., barsabove = True, capsize = 3., mew = 1.)
#     #mew = capthick


# path = os.path.join("data/", params.comp_label, label+"_overall"+params.extension)
# #path = os.path.join(label+"_overall"+params.extension)
# pl.savefig(path, dpi=params.dpi, bbox_inches='tight')


# pl.close('all')



# #########################################################
# #              Single Connecitons
# #########################################################

# pl.clf()

# pl.plot(xs, ps_array, color='red', label='from Perin et al. (2011)')
# pl.plot(xs, 2*p_array*(1-p_array), '--', color = 'blue', label='from overall probability under indepence assumption' )



# ymin, ymax = 0, 0.4
# pl.ylim(ymin,ymax)
# pl.xlim(0,418.6)
# pl.xticks([0,100,200,300,400])
# pl.yticks(np.arange(0,0.45,0.1), ['0.00','0.10','0.20','0.30','0.40'])

# pl.tight_layout()
# #set figure size
# fig = pl.gcf()
# fig.set_size_inches(params.xfigsize,params.yfigsize)

# mew_set = 1.2
# msize = 8
# ypos = 0.195/0.25*(ymax-ymin)
# awidth = 0.001/0.25*(ymax-ymin)
# hwidth = 0.01/0.25*(ymax-ymin)

# ax = pl.gca()
# ax.plot(290,ypos,'o',markersize=msize, color = 'white', mew=mew_set) #mew = markeredgewith!!x
# ax.plot(370,ypos,'o',markersize=msize, color = 'white', mew=mew_set)
# ax.arrow(307.5,ypos, 52-17.5, 0, 
#          width = awidth, head_width=hwidth, head_length=10, fc='k', ec='k')


# pl.xlabel(r'distance in \SI{}{\micro\meter}', fontsize=12, labelpad=8)
# pl.ylabel("probability", fontsize=12, labelpad=11.5)


# path = os.path.join("data/", params.comp_label, label+"_single_empty"+params.extension)
# #path = os.path.join(label+"_single"+params.extension)
# pl.savefig(path, dpi=params.dpi, bbox_inches='tight')


# for data in data_sets:

#     connection_probabilites, bins = data

#     prb_coll = np.array(connection_probabilites["prb_single"])

#     probabilites = np.mean(prb_coll, axis = 0)
#     #standard deviation!
#     errors = np.std(prb_coll, axis = 0)

#     #ps = sp*0.5 + rp
#     bin_centers = (bins[:-1]+bins[1:])/2 

#     pl.errorbar(bin_centers, probabilites, markersize = 2.,yerr=errors, fmt = '.',  color='gray', elinewidth = 2., barsabove = True, capsize = 3., mew = 1., label = 'tuned anisotropic networks')
#     #mew = capthick


# path = os.path.join("data/", params.comp_label, label+"_single"+params.extension)
# #path = os.path.join(label+"_single"+params.extension)
# pl.savefig(path, dpi=params.dpi, bbox_inches='tight')
# pl.close('all')


# #########################################################
# #              Recip Connecitons
# #########################################################

# pl.clf()


# pl.plot(xs, pr_array, color='red')
# pl.plot(xs, p_array**2, '--', color = 'blue')



# ymin, ymax = 0, 0.12
# pl.ylim(ymin,ymax)
# pl.xlim(0,418.6)
# pl.xticks([0,100,200,300,400])
# pl.yticks(np.arange(0,0.13,0.03))

# mew_set = 1.2
# msize = 8
# ypos = 0.195/0.25*(ymax-ymin)
# awidth = 0.001/0.25*(ymax-ymin)
# hwidth = 0.01/0.25*(ymax-ymin)

# ax = pl.gca()
# ax.plot(290,ypos,'o',markersize=msize, color = 'white', mew=mew_set) #mew = markeredgewith!!x
# ax.plot(370,ypos,'o',markersize=msize, color = 'white', mew=mew_set)
# ax.arrow(307.5,ypos+0.0025, 52-17.5, 0, 
#          width = awidth, head_width=hwidth, head_length=10, fc='k', ec='k')
# ax.arrow(307.5+(52-17.5)+10,ypos-0.0025, -(52-17.5) , 0, 
#          width = awidth, head_width=hwidth, head_length=10, fc='k', ec='k')


# pl.tight_layout()
# #set figure size
# fig = pl.gcf()
# fig.set_size_inches(params.xfigsize,params.yfigsize)

# pl.xlabel(r'distance in \SI{}{\micro\meter}', fontsize=12, labelpad=8)
# pl.ylabel("probability", fontsize=12, labelpad=11.5)

# path = os.path.join("data/", params.comp_label, label+"_recip_empty"+params.extension)
# #path = os.path.join(label+"_recip"+params.extension)
# pl.savefig(path, dpi=params.dpi, bbox_inches='tight')


# for data in data_sets:

#     connection_probabilites, bins = data

#     prb_coll = np.array(connection_probabilites["prb_recip"])

#     probabilites = np.mean(prb_coll, axis = 0)
#     #standard deviation!
#     errors = np.std(prb_coll, axis = 0)

#     #ps = sp*0.5 + rp
#     bin_centers = (bins[:-1]+bins[1:])/2 

#     pl.errorbar(bin_centers, probabilites, markersize = 2.,yerr=errors, fmt = '.',  color='gray', elinewidth = 2., barsabove = True, capsize = 3., mew = 1.)
#     #mew = capthick

# path = os.path.join("data/", params.comp_label, label+"_recip"+params.extension)
# #path = os.path.join(label+"_recip"+params.extension)
# pl.savefig(path, dpi=params.dpi, bbox_inches='tight')
# pl.close('all')





# def p_fit(x):

#     '''Fitting the curve from Perin 2011'''

#     a = -1.4186123229540666E-03
#     b = 2.7630272296832398E-03
#     c = -9.4484523305731971E-01
#     Offset = 2.3078566917566815E-01

#     return  a/(b+pow(x,c)) + Offset


# def ps_fit(x):

#     temp = 0.0

#     a = 2.1265459489379471E-01
#     b = -8.2607817023473132E+01
#     c = 2.6606485052456827E+02
#     d = 2.5216202564579659E+00

#     temp = a * math.exp(-0.5 * math.pow((x-b) / c, d))

#     return temp


# def pr_fit(x):

#     a = -1.2451623637345335E-01
#     b = 9.2442483915416082E-03
#     c = 1.1041322663714865E+00
#     offset = 1.2326119868850784E-01

#     return a * math.pow(1.0 - math.exp(-1.0 * b * x), c) + offset

