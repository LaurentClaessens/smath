# -*- coding: utf8 -*-
from phystricks import *
def YGlrtNX():
    pspict,fig = SinglePicture("YGlrtNX")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    f=LagrangePolynomial( [Point(-4,-2),Point(-3,0),Point(-1.5,2),Point(0,0),Point(1,1),Point(2,3),Point(4,0)] ).graph(-4,4)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
