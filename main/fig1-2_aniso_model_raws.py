
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl

import sys
sys.path.append("..")

from utils.colors import color

  
import graph_tool as gt

gpath = '/home/lab/comp/data/aniso-netw'+\
        '_N1000_w37.3_ed-l296_4GX7-00.gt'
g_aniso = gt.load_graph(gpath)



def plot_network_1cell_targets(g, i, save_path, with_nodes=True,
                               with_targets=True, color=color['aniso']):

    pl.clf()
    fig = pl.figure()
    fig.set_size_inches(3.,3.)
    
    ax = fig.add_subplot(111)

    xy = g.vertex_properties["xy"]
    xs = [xy[v][0] for v in g.vertices()]
    ys = [xy[v][1] for v in g.vertices()]

    source = g.vertex(i)
    target_ids = []
    for e in source.out_edges():
        target_ids.append(int(e.target()))

    target_xs = [xs[k] for k in target_ids]
    target_ys = [ys[k] for k in target_ids]

    if with_nodes:
        ax.plot(xs,ys, 'o', markeredgecolor='grey',
                markerfacecolor='grey', markersize=0.5)
    
    if with_targets:
        ax.plot(target_xs, target_ys, 'o', color='r',
                markerfacecolor= color, markeredgecolor= color,
                markersize = 3.)
        
    marker = '^'
    ax.plot(xs[i],ys[i], color = 'white', marker = marker,
            markersize= 11, markeredgewidth=2.)

    ed_l = g.graph_properties["ed_l"]
    ax.set_xlim(0,ed_l)
    ax.set_ylim(0,ed_l)

    ax.text(0.2, 0.01,
            r'\bfseries \textnumero$\,$'+'{:d}'.format(i),
            bbox={'facecolor':'white', 'edgecolor':'white',
                  'pad':0.8}, 
            verticalalignment='bottom',
            horizontalalignment='right',
            transform=ax.transAxes)

    pl.xticks([])
    pl.yticks([])

    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
   
    pl.savefig(save_path, dpi=600,  bbox_inches='tight')




from matplotlib import rc
rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    # helvetica font
    r'\usepackage{textcomp}',
    r'\usepackage{sansmath}',   # math-font matching helvetica
    r'\sansmath'                # actually tell tex to use it!
    r'\usepackage{siunitx}',    # micro symbols
    r'\sisetup{detect-all}'    # force siunitx to use the fonts
]


import os
fname = os.path.splitext(os.path.basename(__file__))[0]


# A -- No. 26, no nodes for source node overlay
plot_network_1cell_targets(g_aniso, 26, fname+'_A_No26_no_nodes.png',
                           with_nodes=False, with_targets=False)
# A -- No. 26, only nodes
plot_network_1cell_targets(g_aniso, 26, fname+'_A_No26_nodes_only.png',
                           with_nodes=True, with_targets=False)
# A -- No. 26, full
plot_network_1cell_targets(g_aniso, 26, fname+'_A_No26_full.png',
                           with_nodes=True, with_targets=True)

# B -- No. 54
plot_network_1cell_targets(g_aniso, 54, fname+'_B_No54.png')

    
