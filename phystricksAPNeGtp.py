# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def APNeGtp():
    pspict,fig = SinglePicture("APNeGtp")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(0.8)

    f=phyFunction(x*(x-1)*(x+3)/2).graph(-3.5,1.5)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
