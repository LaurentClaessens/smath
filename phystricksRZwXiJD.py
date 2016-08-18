# -*- coding: utf8 -*-
from phystricks import *
def RZwXiJD():
    pspict,fig = SinglePicture("RZwXiJD")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)


    I=Segment(cube.E,cube.F).center()
    J=Segment(cube.B,cube.F).center()

    I.put_mark(0.2,90,"\( I\)",pspict=pspict,position="S")
    J.put_mark(0.2,-45,"\( J\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(cube,I,J)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
