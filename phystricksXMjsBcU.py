# -*- coding: utf8 -*-
from phystricks import *
def XMjsBcU():
    pspict,fig = SinglePicture("XMjsBcU")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(0.5)

    f=phyFunction(-2*x+3).graph(-1.5,2)
    f.put_mark(0.2,0,"\( d_1\)",automatic_place=(pspict,"W"))

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
