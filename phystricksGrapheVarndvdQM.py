# -*- coding: utf8 -*-
from phystricks import *
def GrapheVarndvdQM():
    pspict,fig = SinglePicture("GrapheVarndvdQM")
    pspict.dilatation(1)

    x=var('x')
    f=HermiteInterpolation([(-1,-1,0),(1,1,0),(-3,1,-1)]).graph(-2.5,1.5)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
