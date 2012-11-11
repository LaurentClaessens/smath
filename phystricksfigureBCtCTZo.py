# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def plan(A,B,C,D,dilatation):
    """
    retourne le polygone qui correspond au plan donné par 4 points.
    """
    AB=Segment(A,B).dilatation(dilatation)
    CD=Segment(C,D).dilatation(dilatation)
    plan=Polygon(AB.I,AB.F,CD.F,CD.I)
    return plan

def figureBCtCTZo():
    pspict,fig = SinglePicture("figureBCtCTZo")
    pspict.dilatation(1)

    l=3
    dilatation=1
    perspective=ObliqueProjection(30,0.5)
    M = perspective.point(l/2,l/2,l/2)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    M.put_mark(0.2,135,"\( M\)",automatic_place=pspict)
    M.parameters.symbol="x"

    plan1=plan(cube.A,cube.H,cube.B,cube.G,dilatation)
    plan1.no_edges()
    plan1.parameters.filled()
    plan1.parameters.fill.color="brown"

    seg=Segment(cube.F,cube.D).dilatation(1.2)

    pspict.DrawGraphs(plan1,seg,cube,M)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()


