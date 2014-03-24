# -*- coding: utf8 -*-
from phystricks import *
def OCFmVDE():
    pspict,fig = SinglePicture("OCFmVDE")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.25)

    x=var('x')
    f=phyFunction( (x+3)*(x-5) ).graph(-4,6)

    pspict.axes.single_axeY.Dx=2

    pspict.DrawGraphs(f)
    #pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
