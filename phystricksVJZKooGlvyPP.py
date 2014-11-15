# -*- coding: utf8 -*-
from phystricks import *
def VJZKooGlvyPP():
    pspict,fig = SinglePicture("VJZKooGlvyPP")
    pspict.dilatation_Y(0.2)

    pts=[  Point(1,4),Point(2,8),Point(3,12),Point(4,16) ]
    pspict.DrawGraphs(pts)

    pspict.axes.single_axeX.put_mark(0.2,-45,"\( \Omega\)",automatic_place=(pspict,"corner"))
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
