
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl



def plot_network_single_cell_targets(g, i, save_path,
                                     color = '#1f78b4'):

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

    ax.plot(xs,ys, 'o', color='k', markersize=0.5,)
    ax.plot(target_xs, target_ys, 'o', color='r',
            markerfacecolor= color, markeredgecolor= color,
            markersize = 3.)
    marker = '^'
    ax.plot(xs[i],ys[i], color = 'white', marker = marker,
            markersize= 11, markeredgewidth=2.)
    # marker = r'$\bigtriangleup$'
    # ax.plot(xs[i],ys[i], color = 'k', marker = marker, markersize= 13)
 

    ed_l = g.graph_properties["ed_l"]
    ax.set_xlim(0,ed_l)
    ax.set_ylim(0,ed_l)

    ax.text(0.95, 0.01,
            r'\bfseries \textnumero$\,$'+'{:d}'.format(i),
            bbox={'facecolor':'white', 'edgecolor':'white',
                  'pad':1}, 
            verticalalignment='bottom',
            horizontalalignment='right',
            transform=ax.transAxes)

    pl.xticks([])
    pl.yticks([])

    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
   
    pl.savefig(save_path, dpi=300,  bbox_inches='tight')



from utils.colors import color

    
import graph_tool as gt
g_aniso = gt.load_graph('../comp/data/aniso-netw_N1000_w37.3_ed-l296_4GX7-0bae.gt')
g_rew = gt.load_graph('../comp/data/rew-netw_rfrac1.00_efrac0.05_4FU2-0bae.gt')


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

for i in [133]:

    plot_network_single_cell_targets(g_aniso, i, fname+'{:d}a'.format(i), color['aniso'])

    plot_network_single_cell_targets(g_rew, i, fname+'{:d}r'.format(i), color['rew'])
