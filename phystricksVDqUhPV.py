# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def VDqUhPV():
    pspict,fig = SinglePicture("VDqUhPV")
    pspict.dilatation(1)

    x=var('x')
    P=LagrangePolynomial( [  Point(1/2,3),Point(2,3),Point(4,0)    ] ).graph(-2.5,4.5)

    pspict.DrawGraphs(P)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
