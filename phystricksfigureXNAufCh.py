# -*- coding: utf8 -*-
from phystricks import *
def figureXNAufCh():
    pspict,fig = SinglePicture("figureXNAufCh")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(x**2).graph(-2.5,2.5)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
