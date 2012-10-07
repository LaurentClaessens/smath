# -*- coding: utf8 -*-
from phystricks import *
def PrismeCQlZKY():
    pspict,fig = SinglePicture("PrismeCQlZKY")
    pspict.dilatation(0.7)


    l=8
    h=4
    p=4
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,h,p)
    cube.put_vertex_mark(pspict)

    AH=Segment(cube.A,cube.H)
    ED=Segment(cube.E,cube.D)
    AH.parameters.style="dotted"
    ED.parameters.style="dotted"
    I=Intersection(AH,ED)[0]
    BG=Segment(cube.B,cube.G)
    FC=Segment(cube.F,cube.C)
    J=Intersection(BG,FC)[0]
    I.put_mark(0.2,0,"\( I\)",automatic_place=pspict)
    J.put_mark(0.2,0,"\( J\)",automatic_place=pspict)
    IJ=Segment(I,J)
    IJ.parameters.style="dashed"

    pspict.DrawGraphs(AH,ED,BG,FC,I,J,IJ,cube)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
