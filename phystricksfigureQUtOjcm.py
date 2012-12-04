# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *
def figureQUtOjcm():
    pspict,fig = SinglePicture("figureQUtOjcm")
    pspict.dilatation(0.7)

    for i in range(1,6):
        P=Point(i,3*i/2+0.5)
        pspict.DrawGraphs(P)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
