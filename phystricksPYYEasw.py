# -*- coding: utf8 -*-
from phystricks import *
def PYYEasw():
    pspict,fig = SinglePicture("PYYEasw")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    f=phyFunction(x**2).graph(-2,2)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
