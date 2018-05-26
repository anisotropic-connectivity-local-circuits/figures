
import numpy as np


def draw_motifs(ax, i, ymin, ymax,  highlight = False):

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

    frac = 0.3
    alpha = np.arctan(ydist/xdist)
    add_x = np.cos(alpha)*frac*xdist
    add_y = np.sin(alpha)*frac*xdist

    width_rect = xdist*2+0.4*xdist
    height_rect = ydist+0.5*ydist


    positions = [((i-1)+xpos-xdist, ypos),
                 ((i-1)+xpos+xdist, ypos),
                 ((i-1)+xpos, ypos+ydist)]

    arrow_properties = {'length_includes_head': True,
                        'width': awidth,
                        'head_length': 0.1}

    bar_gray =         {'head_width': 0,
                        'fc': a_gray,
                        'ec': a_gray}

    arrow_black =      {'head_width': hwidth,
                        'fc': 'k',
                        'ec': 'k'}

    bar_gray.update(arrow_properties)
    arrow_black.update(arrow_properties)

    if i==1: 
        
        # downleft
        ax.arrow(positions[2][0]-add_x, positions[2][1]-add_y,
                 -xdist+2*add_x, -ydist+2*add_y,
                 **bar_gray)
        #upleft
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x,ydist-2*add_y,
                 **bar_gray)
        # ->
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **bar_gray)


    if i==2:

        # downleft
        ax.arrow(positions[2][0]-add_x, positions[2][1]-add_y,
                 -xdist+2*add_x, -ydist+2*add_y,
                 **arrow_black)

        #upleft
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x, ydist-2*add_y,
                 **bar_gray)
        # ->
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **bar_gray)

    if i==3: 

        ax.arrow(positions[0][0]+add_x, positions[0][1]+add_y,
                 xdist-2*add_x, ydist-2*add_y,
                 **arrow_black)

        # downleft
        ax.arrow(positions[2][0]-add_x, positions[2][1]-add_y,
                 -xdist+2*add_x,-ydist+2*add_y,
                 **arrow_black)
        
        #upleft
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x,ydist-2*add_y,
                 **bar_gray)
        # ->
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **bar_gray)

    if i==4: 

        # downleft
        ax.arrow(positions[2][0]-add_x, positions[2][1]-add_y,
                 -xdist+2*add_x, -ydist+2*add_y,
                 **arrow_black)
        
        #downright
        ax.arrow(positions[2][0]+add_x, positions[2][1]-add_y,
                 xdist-2*add_x, -ydist+2*add_y,
                 **arrow_black)
        # -
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **bar_gray)


    if i==5: 

        ax.arrow(positions[0][0]+add_x, positions[0][1]+add_y,
                 xdist-2*add_x, ydist-2*add_y,
                 **arrow_black)

        #upleft                 
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x, ydist-2*add_y,
                 **arrow_black)
        # -
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **bar_gray)

    if i==6: 

        #  upright
        ax.arrow(positions[0][0]+add_x, positions[0][1]+add_y,
                 xdist-2*add_x, ydist-2*add_y,
                 **arrow_black)
        
        #downright
        ax.arrow(positions[2][0]+add_x, positions[2][1]-add_y,
                 xdist-2*add_x, -ydist+2*add_y,
                 **arrow_black)
        # -
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **bar_gray)
        
    if i==7: 

        ax.arrow(positions[0][0]+add_x, positions[0][1]+add_y,
                 xdist-2*add_x, ydist-2*add_y,
                 **arrow_black)

        #downright
        ax.arrow(positions[2][0]+add_x, positions[2][1]-add_y,
                 xdist-2*add_x, -ydist+2*add_y,
                 **arrow_black)
        
        #upleft
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x, ydist-2*add_y,
                 **arrow_black)
        
        # -
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **bar_gray)

    if i==8:
        
        #upleft
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x, ydist-2*add_y,
                 **arrow_black)

        #downright
        ax.arrow(positions[2][0]+add_x, positions[2][1]-add_y,
                 +xdist-2*add_x, -ydist+2*add_y,
                 **arrow_black)
        
        # downleft
        ax.arrow(positions[2][0]-add_x, positions[2][1]-add_y,
                 -xdist+2*add_x, -ydist+2*add_y,
                 **arrow_black)
        
        # -
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **bar_gray)

    if i==9: 

        #  upright
        ax.arrow(positions[0][0]+add_x, positions[0][1]+add_y,
                 xdist-2*add_x, ydist-2*add_y,
                 **arrow_black)
       
        # downleft
        ax.arrow(positions[2][0]-add_x, positions[2][1]-add_y,
                 -xdist+2*add_x, -ydist+2*add_y,
                 **arrow_black)

        #upleft
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x, ydist-2*add_y,
                 **arrow_black)
        
        #downright
        ax.arrow(positions[2][0]+add_x, positions[2][1]-add_y,
                 +xdist-2*add_x, -ydist+2*add_y,
                 **arrow_black)
        # -
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **bar_gray)

    if i==10:
        
        # downleft
        ax.arrow(positions[2][0]-add_x, positions[2][1]-add_y,
                 -xdist+2*add_x, -ydist+2*add_y,
                 **arrow_black)

        #downright
        ax.arrow(positions[2][0]+add_x, positions[2][1]-add_y,
                 xdist-2*add_x, -ydist+2*add_y,
                 **arrow_black)
        # ->
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **arrow_black)

        
    if i==11: 

        ax.arrow(positions[2][0]-add_x, positions[2][1]-add_y,
                 -xdist+2*add_x, -ydist+2*add_y,
                 **arrow_black)
        #upleft
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x, ydist-2*add_y,
                 **arrow_black)
        # ->
        ax.arrow(frac*xdist+positions[0][0], positions[0][1], 
                 2*xdist-2*frac*xdist, 0,
                 **arrow_black)


    if i == 12:

        #  upright
        ax.arrow(positions[0][0]+add_x, positions[0][1]+add_y, 
                 xdist-2*add_x, ydist-2*add_y,
                 **arrow_black)

        #upleft
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x, ydist-2*add_y,
                 **arrow_black)

        #downright
        ax.arrow(positions[2][0]+add_x, positions[2][1]-add_y,
                 xdist-2*add_x, -ydist+2*add_y,
                 **arrow_black)

        # ->
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **arrow_black)


    if i == 13: 

        # downleft
        ax.arrow(positions[2][0]-add_x, positions[2][1]-add_y,
                 -xdist+2*add_x, -ydist+2*add_y,
                 **arrow_black)
        
        #upleft
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x, ydist-2*add_y,
                 **arrow_black)
        
        #downright
        ax.arrow(positions[2][0]+add_x, positions[2][1]-add_y,
                 +xdist-2*add_x, -ydist+2*add_y,
                 **arrow_black)

        # ->
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **arrow_black)

        
    if i == 14:
        
        # downleft
        ax.arrow(positions[2][0]-add_x, positions[2][1]-add_y,
                 -xdist+2*add_x, -ydist+2*add_y,
                 **arrow_black)

        #upleft
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x, ydist-2*add_y,
                 **arrow_black)

        #downright
        ax.arrow(positions[2][0]+add_x, positions[2][1]-add_y,
                 xdist-2*add_x, -ydist+2*add_y,
                 **arrow_black)

        # <-
        ax.arrow(-frac*xdist+positions[1][0], positions[1][1],
                 -2*xdist+2*frac*xdist, 0,
                 **arrow_black)


    if i == 15: 

        # downleft
        ax.arrow(positions[2][0]-add_x, positions[2][1]-add_y,
                 -xdist+2*add_x, -ydist+2*add_y,
                 **arrow_black)

        #upleft
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x, ydist-2*add_y,
                 **arrow_black)

        #downright
        ax.arrow(positions[2][0]+add_x, positions[2][1]-add_y,
                 xdist-2*add_x, -ydist+2*add_y,
                 **arrow_black)

        #  upright
        ax.arrow(positions[0][0]+add_x, positions[0][1]+add_y,
                 xdist-2*add_x, ydist-2*add_y,
                 **arrow_black)

        # ->
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **arrow_black)


    if i == 16: #Song 16

        # downleft
        ax.arrow(positions[2][0]-add_x, positions[2][1]-add_y,
                 -xdist+2*add_x, -ydist+2*add_y,
                 **arrow_black)

        #upleft
        ax.arrow(positions[1][0]-add_x, positions[1][1]+add_y,
                 -xdist+2*add_x, ydist-2*add_y,
                 **arrow_black)
        
        #downright
        ax.arrow(positions[2][0]+add_x, positions[2][1]-add_y,
                 xdist-2*add_x, -ydist+2*add_y,
                 **arrow_black)
        
        #  upright
        ax.arrow(positions[0][0]+add_x, positions[0][1]+add_y,
                 xdist-2*add_x, ydist-2*add_y,
                 **arrow_black)
        # <-
        ax.arrow(-frac*xdist+positions[1][0], positions[1][1],
                 -2*xdist+2*frac*xdist, 0,
                 **arrow_black)
        # ->
        ax.arrow(frac*xdist+positions[0][0], positions[0][1],
                 2*xdist-2*frac*xdist, 0,
                 **arrow_black)


