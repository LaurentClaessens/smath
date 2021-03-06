# -*- coding: utf8 -*-
from phystricks import *
def CXWooOMPOQT():
    pspict,fig = SinglePicture("CXWooOMPOQT")

    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(1)

    moustaches=[]

    # Le delta_y n'a pas d'importance parce qu'il est recalculé plus bas.
    moustaches.append(Moustache(7.90,10.20,14.45,16.70,20.00,h=0.5,delta_y=0.75))   

    for i,m in enumerate(moustaches) :
        m.delta_y=0.75+i
        m.put_mark(0.2,text="DS {}".format( len(moustaches)-i ),pspict=pspict,position="W")

    pspict.DrawGraphs(moustaches)
    pspict.grid.draw_horizontal_grid=False
    pspict.axes.draw_single_axeY=False
    pspict.axes.single_axeY.no_graduation()
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
