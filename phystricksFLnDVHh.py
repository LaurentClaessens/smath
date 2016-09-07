# -*- coding: utf8 -*-
from phystricks import *
def FLnDVHh():
    pspict,fig = SinglePicture("FLnDVHh")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(-x**2/2+x+3).graph(-2,4)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
