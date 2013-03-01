# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def IQnEPpt():
    pspict,fig = SinglePicture("IQnEPpt")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction((3/2)*x+1).graph(-3,3)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
