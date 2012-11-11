# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *
from phystricksfigureBCtCTZo import plan

def figureASkECWS():
    pspict,fig = SinglePicture("figureASkECWS")
    pspict.dilatation(1)

    l=3
    dilatation=1.5
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    plan1=plan(cube.A,cube.B,cube.E,cube.F,dilatation)
    plan1.no_edges()
    plan1.parameters.filled()
    plan1.parameters.fill.color="brown"

    seg=Segment(cube.H,cube.C).dilatation(1.5)
    seg.parameters.color="red"

    pspict.DrawGraphs(plan1,seg,cube)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


