# -*- coding: utf8 -*-
from phystricks import *
def YAaXJqQ():
    pspict,fig = SinglePicture("YAaXJqQ")
    pspict.dilatation(0.7)

    x=var('x')
    F=phyFunction((1/(x+3))+1).graph(-7,3)
    F.cut_y(-3,5)

    pspict.comment="The graph is cut into two parts around x=-3"
    pspict.DrawGraphs(F)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
