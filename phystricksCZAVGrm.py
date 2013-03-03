# -*- coding: utf8 -*-
from phystricks import *
def CZAVGrm():
    pspict,fig = SinglePicture("CZAVGrm")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(  (x+1)*(x-3)  ).graph(-1.5,3.5)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
