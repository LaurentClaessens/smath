# -*- coding: utf8 -*-
from phystricks import *
def TCpyyhO():
    pspict,fig = SinglePicture("TCpyyhO")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    x=var('x')
    xmin=-1
    xmax=8
    ymin=-0.5
    ymax=12
    g=phyFunction(2*x+1).fit_inside(xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
    h=phyFunction(3*x-4).fit_inside(xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)

    pspict.DrawGraphs(g,h)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
