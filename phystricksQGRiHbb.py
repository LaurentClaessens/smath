# -*- coding: utf8 -*-
from phystricks import *
def QGRiHbb():
    pspict,fig = SinglePicture("QGRiHbb")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    f=phyFunction(x**2-6*x+5).graph(0,4)

    pspict.DrawGraphs(f)
    #pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
