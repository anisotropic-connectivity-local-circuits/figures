
import sys,os,pickle
import itertools

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl
from matplotlib.patches import Rectangle

import numpy as np
from scipy import stats

from utils.colors import color


fpath = '/home/lab/comp/data/three_motif_counts_aniso_S300000.p'

with open(fpath, 'rb') as pfile:
    aniso_data = pickle.load(pfile)


# pfile = open(sys.argv[2], "rb")
# song_data_rew = pickle.load(pfile)
# pfile.close()

# pfile = open(sys.argv[3], "rb")
# song_data_dist_depend = pickle.load(pfile)
# pfile.close()

# try:
#     label = sys.argv[4]
# except IndexError:
#     label = img_label.labelstr



def counts_to_probabilities(df):

    # from dict to array
    data = []
    for key,item in df.iteritems():
        data.append(item)

    song_probs = np.array([np.array(counts)/float(sum(counts)) for counts in data])

    p_means = np.mean(song_probs, axis=0)
    p_errs = stats.sem(song_probs, axis=0)
    
    return p_means, p_errs




def p_from_two_connections(up,s1,s2,rp):
    ''' 
    computes occurrences of three-neuron motifs from 
    neuro pair connection probabilities:

      up   probability for an unconnected pair
      s1   probability for pair with single connection x to y
      s2   probability for pair with single connetion y to x
      rp   probability for reciprocally connected pair 

    '''

    fact = range(17)
    ps = range(17)

    # motifs probabilities below were calculated 
    # from basic combinatorics considerations

    assert s1 == s2
    sp = s1 

    fact[1], ps[1]    =   1, up**3 
    fact[2], ps[2]    =   6, up*up*sp
    fact[3], ps[3]    =   3, up*up*rp
    fact[4], ps[4]    =   3, sp*sp*up
    fact[5], ps[5]    =   3, sp*sp*up
    fact[6], ps[6]    =   6, sp*sp*up
    fact[7], ps[7]    =   6, sp*up*rp
    fact[8], ps[8]    =   6, sp*up*rp
    fact[9], ps[9]    =   3, rp*rp*up
    fact[10],ps[10]   =   6, sp**3   
    fact[11],ps[11]   =   2, sp**3    
    fact[12],ps[12]   =   3, sp*sp*rp
    fact[13],ps[13]   =   6, sp*sp*rp
    fact[14],ps[14]   =   3, sp*sp*rp
    fact[15],ps[15]   =   6, sp*rp*rp
    fact[16],ps[16]   =   1, rp**3     

    del fact[0],ps[0] 

    p = np.array([fact[i]*ps[i] for i in range(len(ps))])

    # Factors should add up to 4^3 = 64 
    # (up, s1, s2 or rp for each of the 3 pairings)
    # and p should add up to 1

    assert sum(fact) == 64
    np.testing.assert_almost_equal(sum(p),1.0, decimal = 10,
                                   err_msg= 'Failed: sum(p) neq 1')

    print "Test: Sum of factors: ", sum(fact), " (Expected: 64)"
    print "Test: Sum of p: ", sum(p), " (Expected: 1.0)"
    
    return p


    

p_mean, p_err = counts_to_probabilities(aniso_data)
# p_mean_dist, p_err_dist = counts_to_probabilities(song_data_dist_depend)
# p_mean_rew, p_err_rew = counts_to_probabilities(song_data_rew)


up = 0.791336
sp = 0.184151
rp = 0.024513  #from mathematica 

# These are the probabilities computed in from the geometric
# considerations in the distance-dependent networks. It was shown (see
# e.g. thesis, but article) that these values are matched in the
# anisotropic networks. Finally, two neuron connection probabilities
# do not change from rewiring.
#
# Taken together, this explains with these values up,sp and rp are
# valid as a reference for computation of expected three motifs in ALL
# three networks.

s1 = sp/2.
s2 = sp/2.

ps = p_from_two_connections(up,s1,s2,rp)


print "\n\n", "---------- Absolute occurrence ----------- "

def print_data_absolute(p_data, p_err, name):

    print "\n", name, ": "
    for j,pp in enumerate(p_data):
        print "  Motif ", j+1, "\t", "occurrence ", pp, "\t", "+- ", p_err[j]

print_data_absolute(p_mean, p_err, "Anisotropic")
# print_data_absolute(p_mean_dist, p_err_dist, "Distance-dependent")
# print_data_absolute(p_mean_rew, p_err_rew, "Rewired")
print "\n"


print "---------- Relative occurrence ----------- "

def print_data_relative(p_data, p_err, norm_data, name):

    print "\n", name, ": "
    for j,pp in enumerate(p_data/norm_data):
        print "  Motif ", j+1, "\t", "rel count: ", pp, "\t", "+- ", p_err[j]/norm_data[j]


print_data_relative(p_mean, p_err, ps, "Anisotropic")
# print_data_relative(p_mean_dist, p_err_dist,  ps, "Distance-dependent")
# print_data_relative(p_mean_rew, p_err_rew, ps, "Rewired")
print "\n"





################################################################
#                   Motif Draw
################################################################


def draw_motifs(i, ymin, ymax,  highlight = False):

    xdist = 0.275
    ydist = 2.4/30.*(ymax-ymin)

    ndist = 0.6
    msize = 2.
    mcolor ='#979797'
    a_gray = '#BDBDBD'
    start = 0.2
    left_in = 0.2
    right_in = 0.2
    mew_set = 1.
    awidth = 0.0001/1.75*(ymax-ymin)
    g_awidth = awidth
    hwidth = 0.025/1.75*(ymax-ymin)
    yoffset = 0.025/1.75*(ymax-ymin)

    xpos = 1.
    ypos = -0.6

    # import matplotlib.image as image

    # img = image.imread('comp/img/arrow.png')
    # fig.figimage(img,xpos,ypos)

    frac = 0.3
    alpha = np.arctan(ydist/xdist)
    add_x = np.cos(alpha)*frac*xdist
    add_y = np.sin(alpha)*frac*xdist

    width_rect = xdist*2+0.4*xdist
    height_rect = ydist+0.5*ydist


    positions = [((i-1)+xpos-xdist, ypos),((i-1)+xpos+xdist, ypos),((i-1)+xpos, ypos+ydist)]


    if i==1: #Song 1
        if not highlight:
            # downleft
            ax.arrow(positions[2][0]-add_x,positions[2][1]-add_y,-xdist+2*add_x,-ydist+2*add_y,
                     width = g_awidth, head_width=0, head_length=0.1, 
                     fc=a_gray, ec=a_gray, length_includes_head= True)
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = g_awidth, head_width=0, head_length=0.1, 
                     fc=a_gray, ec=a_gray, length_includes_head= True)
            # ->
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                 width = g_awidth, head_width=0, head_length=0.1, 
                     fc=a_gray, ec=a_gray, length_includes_head= True)


    if i==2: #Song 2
        if not highlight:
            # downleft
            ax.arrow(positions[2][0]-add_x,positions[2][1]-add_y,-xdist+2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = g_awidth, head_width=0, head_length=0.1, 
                     fc=a_gray, ec=a_gray, length_includes_head= True)
            # ->
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                 width = g_awidth, head_width=0, head_length=0.1, 
                     fc=a_gray, ec=a_gray, length_includes_head= True)

    if i==3: #Song 3
        if not highlight:
            #  upright
            ax.arrow(positions[0][0]+add_x,positions[0][1]+add_y,xdist-2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)

            # downleft
            ax.arrow(positions[2][0]-add_x,positions[2][1]-add_y,-xdist+2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = g_awidth, head_width=0, head_length=0.1, 
                     fc=a_gray, ec=a_gray, length_includes_head= True)
            # ->
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                 width = g_awidth, head_width=0, head_length=0.1, 
                     fc=a_gray, ec=a_gray, length_includes_head= True)


    if i==4: #Song 4
        if highlight:
            ax.add_patch(Rectangle((positions[0][0]+xdist - width_rect/2., 
                                    positions[0][1]+ydist/2. - height_rect/2.), 
                                   width_rect, height_rect, 
                                   facecolor = 'white', edgecolor = 'red'))
        else:
            # downleft
            ax.arrow(positions[2][0]-add_x,positions[2][1]-add_y,-xdist+2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #downright
            ax.arrow(positions[2][0]+add_x,positions[2][1]-add_y,+xdist-2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)  
            # -
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                 width = g_awidth, head_width=0, head_length=0.1, 
                 fc=a_gray, ec=a_gray, length_includes_head= True)

            

    if i==5: #Song 5
        if not highlight:
            #  upright
            ax.arrow(positions[0][0]+add_x,positions[0][1]+add_y,xdist-2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            # -
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                 width = g_awidth, head_width=0, head_length=0.1, 
                 fc=a_gray, ec=a_gray, length_includes_head= True)

    if i==6: #Song 6
        if not highlight:
            #  upright
            ax.arrow(positions[0][0]+add_x,positions[0][1]+add_y,xdist-2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #downright
            ax.arrow(positions[2][0]+add_x,positions[2][1]-add_y,+xdist-2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            # -
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                 width = g_awidth, head_width=0, head_length=0.1, 
                 fc=a_gray, ec=a_gray, length_includes_head= True)

    if i==7: #Song 7
        if not highlight:
            #  upright
            ax.arrow(positions[0][0]+add_x,positions[0][1]+add_y,xdist-2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #downright
            ax.arrow(positions[2][0]+add_x,positions[2][1]-add_y,+xdist-2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            # -
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                 width = g_awidth, head_width=0, head_length=0.1, 
                 fc=a_gray, ec=a_gray, length_includes_head= True)

    if i==8: #Song 8
        # if highlight:
        #     ax.add_patch(Rectangle((positions[0][0]+xdist - width_rect/2., 
        #                             positions[0][1]+ydist/2. - height_rect/2.), 
        #                            width_rect, height_rect, 
        #                            facecolor = 'white', edgecolor = 'red'))

        if not highlight:
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #downright
            ax.arrow(positions[2][0]+add_x,positions[2][1]-add_y,+xdist-2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            # downleft
            ax.arrow(positions[2][0]-add_x,positions[2][1]-add_y,-xdist+2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            # -
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                 width = g_awidth, head_width=0, head_length=0.1, 
                 fc=a_gray, ec=a_gray, length_includes_head= True)

    if i==9: #Song 9
        if not highlight:
            #  upright
            ax.arrow(positions[0][0]+add_x,positions[0][1]+add_y,xdist-2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            # downleft
            ax.arrow(positions[2][0]-add_x,positions[2][1]-add_y,-xdist+2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #downright
            ax.arrow(positions[2][0]+add_x,positions[2][1]-add_y,+xdist-2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            # -
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                 width = g_awidth, head_width=0, head_length=0.1, 
                 fc=a_gray, ec=a_gray, length_includes_head= True)

    if i==10: #Song 10
        if highlight:
            ax.add_patch(Rectangle((positions[0][0]+xdist - width_rect/2., 
                                    positions[0][1]+ydist/2. - height_rect/2.), 
                                   width_rect, height_rect, 
                                   facecolor = 'white', edgecolor = 'red'))
        else:
            # downleft
            ax.arrow(positions[2][0]-add_x,positions[2][1]-add_y,-xdist+2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #downright
            ax.arrow(positions[2][0]+add_x,positions[2][1]-add_y,+xdist-2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            # ->
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                 width = awidth, head_width=hwidth, head_length=0.1, 
                 fc='k', ec='k', length_includes_head= True)




    if i==11: #Song 11
        if not highlight:
            # downleft
            ax.arrow(positions[2][0]-add_x,positions[2][1]-add_y,-xdist+2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            # ->
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                 width = awidth, head_width=hwidth, head_length=0.1, 
                 fc='k', ec='k', length_includes_head= True)

    if i == 12: #Song 12

        if highlight:
            ax.add_patch(Rectangle((positions[0][0]+xdist - width_rect/2., 
                                    positions[0][1]+ydist/2. - height_rect/2.), 
                                   width_rect, height_rect, 
                                   facecolor = 'white', edgecolor = 'red'))
        else:

            #  upright
            ax.arrow(positions[0][0]+add_x,positions[0][1]+add_y,xdist-2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #downright
            ax.arrow(positions[2][0]+add_x,positions[2][1]-add_y,+xdist-2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)        # ->
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)

    if i == 13: #Song 13
        if not highlight:
            # downleft
            ax.arrow(positions[2][0]-add_x,positions[2][1]-add_y,-xdist+2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #downright
            ax.arrow(positions[2][0]+add_x,positions[2][1]-add_y,+xdist-2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)        # ->
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)

    if i == 14: #Song 14

        if highlight:
            ax.add_patch(Rectangle((positions[0][0]+xdist - width_rect/2., 
                                    positions[0][1]+ydist/2. - height_rect/2.), 
                                   width_rect, height_rect, 
                                   facecolor = 'white', edgecolor = 'red'))

        else:
            # downleft
            ax.arrow(positions[2][0]-add_x,positions[2][1]-add_y,-xdist+2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #downright
            ax.arrow(positions[2][0]+add_x,positions[2][1]-add_y,+xdist-2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            # <-
            ax.arrow(-frac*xdist+positions[1][0],positions[1][1],-2*xdist+2*frac*xdist,0,
                 width = awidth, head_width=hwidth, head_length=0.1, 
                 fc='k', ec='k', length_includes_head= True)


    if i == 15: #Song 15

        if highlight:
            ax.add_patch(Rectangle((positions[0][0]+xdist - width_rect/2., 
                                    positions[0][1]+ydist/2. - height_rect/2.), 
                                   width_rect, height_rect, 
                                   facecolor = 'white', edgecolor = 'red'))

        else:
            # downleft
            ax.arrow(positions[2][0]-add_x,positions[2][1]-add_y,-xdist+2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #downright
            ax.arrow(positions[2][0]+add_x,positions[2][1]-add_y,+xdist-2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #  upright
            ax.arrow(positions[0][0]+add_x,positions[0][1]+add_y,xdist-2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)

            # ->
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)


    if i == 16: #Song 16

        if highlight:
            ax.add_patch(Rectangle((positions[0][0]+xdist - width_rect/2., 
                                    positions[0][1]+ydist/2. - height_rect/2.), 
                                   width_rect, height_rect, 
                                   facecolor = 'white', edgecolor = 'red'))

        else:
            # downleft
            ax.arrow(positions[2][0]-add_x,positions[2][1]-add_y,-xdist+2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #upleft
            ax.arrow(positions[1][0]-add_x,positions[1][1]+add_y,-xdist+2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #downright
            ax.arrow(positions[2][0]+add_x,positions[2][1]-add_y,+xdist-2*add_x,-ydist+2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)
            #  upright
            ax.arrow(positions[0][0]+add_x,positions[0][1]+add_y,xdist-2*add_x,ydist-2*add_y,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)

            # <-
            ax.arrow(-frac*xdist+positions[1][0],positions[1][1],-2*xdist+2*frac*xdist,0,
                 width = awidth, head_width=hwidth, head_length=0.1, 
                 fc='k', ec='k', length_includes_head= True)
            # ->
            ax.arrow(frac*xdist+positions[0][0],positions[0][1],2*xdist-2*frac*xdist,0,
                     width = awidth, head_width=hwidth, head_length=0.1, 
                     fc='k', ec='k', length_includes_head= True)






lbl_fntsz = 10
tick_fntsz = 9

from matplotlib import rc
 
rc('text', usetex=True)
pl.rcParams['text.latex.preamble'] = [
    r'\usepackage{tgheros}',    # helvetica font
    r'\usepackage{sansmath}',   # math-font matching  helvetica
    r'\sansmath'                # actually tell tex to use it!
    r'\usepackage{siunitx}',    # micro symbols
    r'\sisetup{detect-all}',    # force siunitx to use the fonts
]  



pl.rcParams['xtick.major.pad']=+45

fig = pl.figure(facecolor="white")
fig.set_size_inches(7,2.25)
ax = fig.add_subplot(111)

ax.tick_params(axis='both', which='major', labelsize=tick_fntsz)

ax.set_xlim(0.,16+1.25)
ymin = -1
ymax = 5
ax.set_ylim(ymin, ymax)

ax.spines['bottom'].set_position(('data',1))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('none')
#ax.yaxis.set_ticks_position('left')

pl.ylabel('relative counts', size=lbl_fntsz)

capsz = 3.25
cpt = 1.5
errlw = 1.5
mew = 1.5

# capsz = 0
# cpt = 0
# errlw = 0
# mew = 0

lw = 3.
opacity = 0.25
opacity_aniso = 0.6

bwidth = 0.5

err_dict = dict(ecolor='red', lw=errlw, capsize=capsz, capthick=cpt, mew = mew)
# err_dict_dist = dict(ecolor='k', lw=errlw, capsize=capsz, capthick=cpt, mew = mew)
# err_dict_rew = dict(ecolor='k', lw=errlw, capsize=capsz, capthick=cpt, mew = mew)

# # Motifs 15 and 16 get divided by 2 to bring them on 5 scale size
# plot_vals_dist = (p_mean_dist/ps)-1
# plot_vals_dist[-1] = plot_vals_dist[-1]/2.
# plot_vals_dist[-2] = plot_vals_dist[-2]/2.

# p_err_vals_dist = p_err_dist/ps
# p_err_vals_dist[-1] = p_err_vals_dist[-1]/2.
# p_err_vals_dist[-2] = p_err_vals_dist[-2]/2.

# # hatch='///////'

# xs_dist = np.array([k-0.00 for k in range(1,len(p_mean)+1)])

# dist_patches = ax.bar(xs_dist, plot_vals_dist, bwidth, linewidth=lw, bottom = 1., edgecolor=color.dist, facecolor = 'white', zorder=1)

# dist_fill = ax.bar(xs_dist, plot_vals_dist, bwidth, bottom = 1., edgecolor=color.dist, facecolor = color.dist, alpha=opacity,  zorder = 2)

# _, caplines, _ = ax.errorbar(xs_dist + bwidth/2., plot_vals_dist+1, fmt='none', yerr = p_err_vals_dist, lw=errlw, capsize=capsz, capthick=cpt, mew = mew, zorder = 3, ecolor=color.dist)

# for capline in caplines:
#     capline.set_zorder(3)


# # Motifs 15 and 16 get divided by 2 to bring them on 5 scale size
# plot_vals_rew = (p_mean_rew/ps)-1
# plot_vals_rew[-1] = plot_vals_rew[-1]/2.
# plot_vals_rew[-2] = plot_vals_rew[-2]/2.

# p_err_vals_rew = p_err_rew/ps
# p_err_vals_rew[-1] = p_err_vals_rew[-1]/2.
# p_err_vals_rew[-2] = p_err_vals_rew[-2]/2.

# xs_rew = np.array([k-0.125 for k in range(1,len(p_mean)+1)])

# rew_patches = ax.bar(xs_rew, plot_vals_rew, bwidth, linewidth=lw, bottom = 1., edgecolor=color.rew, facecolor = 'white', zorder=4)

# rew_fill = ax.bar(xs_rew, plot_vals_rew, bwidth, bottom = 1., edgecolor=color.rew, facecolor = color.rew, alpha = opacity, zorder=5)

# _, caplines, _ = ax.errorbar(xs_rew + bwidth/2., plot_vals_rew+1, fmt='none', yerr = p_err_vals_rew, lw=errlw, capsize=capsz, capthick=cpt, mew = mew, zorder = 6, ecolor = color.rew)

# for capline in caplines:
#     capline.set_zorder(6)


# Motifs 15 and 16 get divided by 2 to bring them on 5 scale size
plot_vals = (p_mean/ps)-1

# for j,val in enumerate(plot_vals):
#     print j+1, "%.2f" %val

# print "\n"

plot_vals[-1] = plot_vals[-1]/2.
plot_vals[-2] = plot_vals[-2]/2.

p_err_vals = p_err/ps
p_err_vals[-1] = p_err_vals[-1]/2.
p_err_vals[-2] = p_err_vals[-2]/2.

# for j,val in enumerate(plot_vals):
#     print j+1, "%.2f" %val

xs_aniso = np.array([k-0.250 for k in range(1,len(p_mean)+1)])

aniso_patches = ax.bar(xs_aniso, plot_vals, bwidth, bottom = 1., edgecolor = color['aniso'], facecolor = 'white', linewidth=lw, zorder=7)

aniso_fill = ax.bar(xs_aniso, plot_vals, bwidth, bottom = 1., edgecolor = color['aniso'], facecolor = color['aniso'], alpha=opacity_aniso, zorder=8)

_, caplines, _ = ax.errorbar(xs_aniso+bwidth/2., plot_vals+1, fmt='none', yerr = p_err_vals, lw=errlw, capsize=capsz, capthick=cpt, mew = mew, zorder = 9, ecolor = color['aniso'])

for capline in caplines:
    capline.set_zorder(9)

def correct_bar_sizes(xs, ys, patches):

    clip_boxes = [pl.Rectangle([x,0], bwidth, y,) for x,y in zip(xs,ys)]

    for clip_box,bar in zip(clip_boxes,patches):
        bar.set_clip_path(clip_box.get_path(), bar.get_transform())


correct_bar_sizes(xs_aniso, plot_vals, aniso_patches)
correct_bar_sizes(xs_aniso, plot_vals, aniso_fill)

# correct_bar_sizes(xs_rew, plot_vals_rew, rew_patches)
# correct_bar_sizes(xs_rew, plot_vals_rew, rew_fill)

# correct_bar_sizes(xs_dist, plot_vals_dist, dist_patches)
# correct_bar_sizes(xs_dist, plot_vals_dist, dist_fill)


for i in range(1,17):
    draw_motifs(i, ymin, ymax, highlight=False)

xrect=0.9225
ystart=4.655
ydist=0.745

ax.add_patch(Rectangle((xrect,ystart), 0.75, 0.2, facecolor = 'white', edgecolor = color['aniso'])) 
ax.add_patch(Rectangle((xrect,ystart), 0.75, 0.2, facecolor = color['aniso'], edgecolor = color['aniso'], alpha=opacity_aniso)) 
fig.text(0.225,0.85, r'anisotropic', color = 'k', fontsize=lbl_fntsz)

# ax.add_patch(Rectangle((xrect,ystart-ydist), 0.75, 0.2, facecolor = 'white', edgecolor=color.rew))
# ax.add_patch(Rectangle((xrect,ystart-ydist), 0.75, 0.2, facecolor = color.rew, edgecolor=color.rew, alpha=opacity))
# fig.text(0.225,0.75, r'rewired', color = 'black', fontsize=lbl_fntsz)

# ax.add_patch(Rectangle((xrect,ystart-2*ydist), 0.75, 0.2, facecolor = 'white', edgecolor=color.dist))
# ax.add_patch(Rectangle((xrect,ystart-2*ydist), 0.75, 0.2, facecolor = color.dist, edgecolor=color.dist, alpha=opacity))
# fig.text(0.225,0.65, r'distance-dependent', color = 'black', fontsize=lbl_fntsz)


#pl.savefig(path, dpi=params.dpi, bbox_inches='tight')

# for i in range(13):
#     draw_motifs(i, ymin, ymax, highlight=True)









ax2 = ax.twinx()
for tl in ax2.get_yticklabels():
    tl.set_color('k')
    tl.set_fontsize(tick_fntsz)

# Math:
# left axis: -1 to 1 and 1 to 5
# right axis: -x to 1 and 1 to 9
# 2/4 = (x+1)/8 => x=3

ax2.set_ylim(-3,9)
ax2.yaxis.set_ticks(range(0,10,2))

ax2.spines['bottom'].set_position(('data',1))
ax2.spines['left'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.xaxis.set_ticks_position('none')


## Testing the double axis set-up
## Motifs 15 and 16 get divided by 6 to bring them on 5 scale size
#plot_vals = (p_mean/ps)-1

#ax2.bar([k-0.350 for k in range(1,len(p_mean)+1)], plot_vals, 0.5, bottom = 1., edgecolor = 'g', facecolor = 'g', yerr = p_err/ps, error_kw=dict(ecolor='red', lw=1.5, capsize=5, capthick=10, mew = 1.5))


pl.xticks(range(1,17))
#ax.xaxis.set_ticks(range(1,14),[str(i) for i in range(4,17)])


# path = os.path.join("data/", params.comp_label, label+params.extension)
path='fig3.png'
fig.savefig(path, dpi=300, bbox_inches='tight')

#fig.savefig("/users/hoffmann/Downloads/"+label+params.extension, dpi=params.dpi, bbox_inches='tight')

pl.close('all')
