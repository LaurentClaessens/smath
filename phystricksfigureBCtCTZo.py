# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def figureBCtCTZo():
    pspict,fig = SinglePicture("figureBCtCTZo")
    pspict.dilatation(1)
    l=3
    dilatation=2
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    AB=Segment(cube.A,cube.B).dilatation(dilatation)
    EF=Segment(cube.E,cube.F).dilatation(dilatation)
    plan1=Polygon(AB.I,AB.F,EF.F,EF.I)
    plan1.no_edges()
    plan1.parameters.filled()
    plan1.parameters.fill.color="brown"

    s1=Segment(cube.D,cube.B).dilatation(1.5)
    s1.parameters.color="red"

    pspict.DrawGraphs(plan1,s1,cube)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
