# -*- coding: utf8 -*-
from phystricks import *
def LignesCubeshBfjxk():
    pspict,fig = SinglePicture("LignesCubeshBfjxk")
    pspict.dilatation(1)

    l=3.5
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    seg1=Segment(cube.c1[2],cube.c2[1])
    seg2=Segment(cube.c1[1],cube.c2[2])
    seg1.parameters.color="red"
    seg2.parameters.color="red"

    seg3=Segment(cube.c2[0],cube.c1[2])
    seg4=Segment(cube.c2[3],cube.c1[1])
    seg3.parameters.color="blue"
    seg4.parameters.color="blue"

    pspict.DrawGraphs(cube,seg1,seg2,seg3,seg4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
