# -*- coding: utf8 -*-
from phystricks import *
def WYeESAN():
    pspict,fig = SinglePicture("WYeESAN")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    l=[  Point(-5,0),Point(-1,2),Point(1,-3),Point(3,7),Point(9,2),Point(10,5) ]

    pspict.DrawGraphs(l)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
