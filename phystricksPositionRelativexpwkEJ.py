# -*- coding: utf8 -*-
from phystricks import *
def PositionRelativexpwkEJ():
    pspict,fig = SinglePicture("PositionRelativexpwkEJ")
    pspict.dilatation(1)

    l=3
    dilatation=1.5
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    BH=Segment(cube.B,cube.H).dilatation(dilatation)
    BH.parameters.color="red"

    pspict.DrawGraphs(cube,BH)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
