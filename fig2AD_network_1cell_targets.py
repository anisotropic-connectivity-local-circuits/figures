
import matplotlib as mpl
mpl.use('Agg')
import pylab as pl

from core import plot_network_1cell_targets

from utils.colors import color

    
import graph_tool as gt
g_aniso = gt.load_graph('../comp/data/aniso-netw_N1000_w37.3_ed-l296_4GX7-0bae.gt')
g_rew = gt.load_graph('../comp/data/rew-netw_rfrac1.00_efrac0.05_4FU2-0bae.gt')
g_dist = gt.load_graph('../comp/data/dist-an-netw_N1000_w37.3_ed-l296_8CY2-0293.gt')
g_tuned = gt.load_graph('../comp/data/tuned-an-netw_N1000_ed-l296_XY51-f4d7.gt')


import os
fname = os.path.splitext(os.path.basename(__file__))[0]

for i in [133]:

    plot_network_1cell_targets(g_aniso, i,
                               fname+'_{:d}-aniso'.format(i),
                               color['aniso'])
    plot_network_1cell_targets(g_rew, i,
                               fname+'_{:d}-rew'.format(i),
                               color['rew'])
for i in [91]:
    plot_network_1cell_targets(g_dist, i,
                               fname+'_{:d}-dist'.format(i),
                               color['dist'])

for i in [11]: 
    # 11,79, 127, 131, 149
    plot_network_1cell_targets(g_tuned, i,
                               fname+'_{:d}-tuned'.format(i),
                               color['tuned'])

    
