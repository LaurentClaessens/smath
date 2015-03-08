# -*- coding: utf8 -*-
from phystricks import *
def ZUZXooIFCxcB():
    pspict,fig = SinglePicture("ZUZXooIFCxcB")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    pspict.DrawGraphs(cube)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
