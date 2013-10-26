# -*- coding: utf8 -*-
from phystricks import *
def MEzTDZC():
    pspict,fig = SinglePicture("MEzTDZC")
    pspict.dilatation(1)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    triangle=Polygon(cube.A,cube.E,cube.F)
    triangle.parameters.filled()
    triangle.parameters.fill.color="lightgray"

    parall=Polygon(cube.A,cube.B,cube.G,cube.H)
    parall.parameters.filled()
    parall.parameters.fill.color="lightgray"


    pspict.DrawGraphs(triangle,parall,cube)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
