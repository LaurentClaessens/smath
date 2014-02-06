# -*- coding: utf8 -*-
from phystricks import *
def WTVlzUE():
    pspict,fig = SinglePicture("WTVlzUE")
    pspict.dilatation_X(0.4)
    pspict.dilatation_Y(0.4)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),13,5,6)
    cube.put_vertex_mark(pspict)

    dilatation=1.6
    diag=Segment(cube.D,cube.F)
    pdiag=Segment(cube.D,cube.G)
    diag.parameters.color="red"
    pdiag.parameters.color="red"

    pspict.DrawGraphs(cube,diag,pdiag)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
