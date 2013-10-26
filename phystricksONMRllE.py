# -*- coding: utf8 -*-
from phystricks import *
def ONMRllE():
    pspict,fig = SinglePicture("ONMRllE")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    I=Segment(cube.A,cube.E).center()
    J=Segment(cube.C,cube.G).center()
    I.put_mark(0.2,135,"\( I\)",automatic_place=(pspict,"S"))
    J.put_mark(0.2,-45,"\( J\)",automatic_place=(pspict,"N"))

    pspict.DrawGraphs(I,J,cube)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
