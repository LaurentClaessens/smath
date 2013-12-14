# -*- coding: utf8 -*-
from phystricks import *
def GSfDCyx():
    pspict,fig = SinglePicture("GSfDCyx")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(1)

    moustache_DS_D1=Moustache(1.5,6.5,9.75,14.025,17.0,h=0.5,delta_y=2.75)
    moustache_DS_D2=Moustache(1.0,8.5,12.0,14.5,19.0,h=0.5,delta_y=1.75)
    moustache_DS_D3=Moustache(0.0,8.1,11.0,14.0,17.5,h=0.5,delta_y=0.75)

    moustache_DS_D1.put_mark(0.2,0,"DS 1",automatic_place=(pspict,"W"))
    moustache_DS_D2.put_mark(0.2,0,"DS 2",automatic_place=(pspict,"W"))
    moustache_DS_D3.put_mark(0.2,0,"DS 3",automatic_place=(pspict,"W"))

    pspict.DrawGraphs(moustache_DS_D1,moustache_DS_D2,moustache_DS_D3)
    pspict.grid.draw_horizontal_grid=False
    pspict.axes.draw_single_axeY=False
    pspict.axes.single_axeY.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
