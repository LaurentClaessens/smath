# -*- coding: utf8 -*-
from phystricks import *
def UZOQooTSAQcl():
    pspict,fig = SinglePicture("UZOQooTSAQcl")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(5,0)
    C=Point(4,2)
    triangle=Polygon(A,B,C)

    triangle.put_mark(0.2,pspict=pspict)
    parallel=triangle.edges[0].parallel_trough(C).dilatation(1.5)
    triangle.edges[0]=triangle.edges[0].dilatation(1.3)

    pspict.DrawGraphs(triangle)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
