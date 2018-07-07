
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl


def correct_bars(xs, ys, patches, bwidth):

    clip_boxes = [pl.Rectangle([x,0], bwidth, y,) for x,y in zip(xs,ys)]

    for clip_box,bar in zip(clip_boxes,patches):
        bar.set_clip_path(clip_box.get_path(), bar.get_transform())


def align_yaxis(ax1, v1, ax2, v2):
    '''
    adjust ax2 ylimit so that v2 in ax2 
    is aligned to v1 in ax1

    taken from https://stackoverflow.com/a/10482477/692634
    '''
    _, y1 = ax1.transData.transform((0, v1))
    _, y2 = ax2.transData.transform((0, v2))
    inv = ax2.transData.inverted()
    _, dy = inv.transform((0, 0)) - inv.transform((0, y1-y2))
    miny, maxy = ax2.get_ylim()
    ax2.set_ylim(miny+dy, maxy+dy)



def errorbars_clip_false(ax, errs):
    '''
    sets clip_on=False for ALL ax.errborbar()
    elements, as the function argument only 
    sets clip_on=False for markers
    see https://stackoverflow.com/questions/2842123

    ax   : axes element
    errs : return of ax.errorbar()
    '''

    for lines in errs[1:]:
        for l in lines:
            l.set_clip_on(False)

    
