
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
                 +xdist-2*add_x, -ydist+2*add_y,
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

    if i==6: #Song 6

        #  upright
        ax.arrow(positions[0][0]+add_x, positions[0][1]+add_y,
                 xdist-2*add_x, ydist-2*add_y,
                 **arrow_black)
        
        #downright
        ax.arrow(positions[2][0]+add_x, positions[2][1]-add_y,
                 xdist-2*add_x, -ydist+2*add_y,
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


