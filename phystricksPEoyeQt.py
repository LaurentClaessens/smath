# -*- coding: utf8 -*-
from phystricks import *
def PEoyeQt():
    pspict,fig = SinglePicture("PEoyeQt")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(1)

    moustache_DS_A1=Moustache(2.5,6.5,8.5,11.5,17.0,h=0.5,delta_y=2.75)
    moustache_DS_A2=Moustache(1.0,5.5,7,11.4,19.0,h=0.5,delta_y=1.75)
    moustache_DS_A3=Moustache(3.0,5.6,7.5,10.9,15.5,h=0.5,delta_y=0.75)

    moustache_DS_A1.put_mark(0.2,0,"DS 1",automatic_place=(pspict,"W"))
    moustache_DS_A2.put_mark(0.2,0,"DS 2",automatic_place=(pspict,"W"))
    moustache_DS_A3.put_mark(0.2,0,"DS 3",automatic_place=(pspict,"W"))

    pspict.DrawGraphs(moustache_DS_A1,moustache_DS_A2,moustache_DS_A3)
    pspict.grid.draw_horizontal_grid=False
    pspict.axes.draw_single_axeY=False
    pspict.axes.single_axeY.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
