# -*- coding: utf8 -*-
from phystricks import *
def PositionPlansTvKvah():
    pspict,fig = SinglePicture("PositionPlansTvKvah")
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
    plan1.parameters.fill.color="red"

    DC=Segment(cube.D,cube.C).dilatation(dilatation)
    HG=Segment(cube.H,cube.G).dilatation(dilatation)
    plan2=Polygon(DC.I,DC.F,HG.F,HG.I)
    plan2.no_edges()
    plan2.parameters.filled()
    plan2.parameters.fill.color="brown"

    pspict.DrawGraphs(plan1,plan2,cube)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
