# -*- coding: utf8 -*-
from phystricks import *
def YAaXJqQ():
    pspict,fig = SinglePicture("YAaXJqQ")
    pspict.dilatation(0.7)

    epsilon=0.2

    x=var('x')
    F=phyFunction((1/(x+3))+1).graph(-7,3)
    F.cut_y(-3,5)

    pspict.DrawGraphs(F)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
