# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *
from phystricksfigureASkECWS import plan

def figureCSIQETx():
    pspict,fig = SinglePicture("figureCSIQETx")
    pspict.dilatation(1)

    l=3
    dilatation=1.5
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    plan1=plan(cube.A,cube.B,cube.E,cube.F,dilatation)
    plan1.no_edges()
    plan1.filled()
    plan1.fill_parameters.color="brown"

    seg=Segment(cube.E,cube.B).dilatation(1.5)
    seg.parameters.color="red"

    pspict.DrawGraphs(plan1,seg,cube)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
