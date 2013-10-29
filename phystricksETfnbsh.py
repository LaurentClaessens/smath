# -*- coding: utf8 -*-
from phystricks import *
def ETfnbsh():
    pspict,fig = SinglePicture("ETfnbsh")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    dilatation=1.6
    s1=Segment(cube.A,cube.H).dilatation(dilatation)
    s2=Segment(cube.E,cube.D).dilatation(dilatation)
    s1.parameters.color="red"
    s2.parameters.color="red"

    pspict.DrawGraphs(s1,s2,cube)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
