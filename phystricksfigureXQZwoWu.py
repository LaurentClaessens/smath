# -*- coding: utf8 -*-
from phystricks import *
def figureXQZwoWu():
    pspict,fig = SinglePicture("figureXQZwoWu")
    pspict.dilatation(1)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    trig=Polygon(cube.A,cube.F,cube.C)
    trig.filled()
    trig.fill_parameters.color="green"
    trig.edges_parameters.color="cyan"

    I=Segment(cube.A,cube.F).midpoint()
    h=Segment(I,cube.C)
    h.parameters.color="red"
    h.parameters.style="dashed"

    I.put_mark(0.2,90,"\( I\)",pspict=pspict)
    
    pspict.DrawGraphs(trig,h,I,cube)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
