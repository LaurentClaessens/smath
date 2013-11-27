# -*- coding: utf8 -*-
from phystricks import *
def PositionPlansqSltxa():
    pspict,fig = SinglePicture("PositionPlansqSltxa")
    pspict.dilatation(1)

    l=3
    dilatation=0.2
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    AH=Segment(cube.A,cube.H).dilatationI(dilatation)
    BG=Segment(cube.B,cube.G).dilatationI(dilatation)
    plan1=Polygon(AH.I,AH.F,BG.F,BG.I)
    plan1.no_edges()
    plan1.parameters.filled()
    plan1.parameters.fill.color="red"

    dilatation=0.4
    DH=Segment(cube.D,cube.H).dilatationI(dilatation)
    CG=Segment(cube.C,cube.G).dilatationI(dilatation)
    plan2=Polygon(DH.I,DH.F,CG.F,CG.I)
    plan2.no_edges()
    plan2.parameters.filled()
    plan2.parameters.fill.color="brown"

    HG=Segment(cube.H,cube.G).dilatation(1.5)
    HG.parameters.color="red"


    pspict.DrawGraphs(plan1,plan2,HG,cube)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
