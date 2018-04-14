
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl


def correct_bars(xs, ys, patches, bwidth):

    clip_boxes = [pl.Rectangle([x,0], bwidth, y,) for x,y in zip(xs,ys)]

    for clip_box,bar in zip(clip_boxes,patches):
        bar.set_clip_path(clip_box.get_path(), bar.get_transform())
