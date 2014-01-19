# -*- coding: utf8 -*-
from phystricks import *
def PEoyeQt():
    pspict,fig = SinglePicture("PEoyeQt")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(1)

    moustaches=[]

    moustaches.append(Moustache(2.0,7.5,10.0,12.0,19.5,h=0.5,delta_y=0.75))     #DS4
    moustaches.append(Moustache(3.0,5.6,7.5,10.9,15.5,h=0.5,delta_y=0.75))      #DS3
    moustaches.append(Moustache(1.0,5.5,7,11.4,19.0,h=0.5,delta_y=1.75))        #DS2
    moustaches.append(Moustache(2.5,6.5,8.5,11.5,17.0,h=0.5,delta_y=2.75))      #DS1

    for i,m in enumerate(moustaches) :
        m.delta_y=0.75+i
        m.put_mark(0.2,0,"DS {}".format( len(moustaches)-i ),automatic_place=(pspict,"W"))

    pspict.DrawGraphs(moustaches)
    pspict.grid.draw_horizontal_grid=False
    pspict.axes.draw_single_axeY=False
    pspict.axes.single_axeY.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
