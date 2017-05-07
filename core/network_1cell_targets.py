
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl


def plot_network_1cell_targets(g, i, save_path,
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
