# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def SurfaceCubeXlLEEy():
    pspict,fig = SinglePicture("SurfaceCubeXlLEEy")
    pspict.dilatation(1)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    I=perspective.point(l/2,l/2,0)
    J=perspective.point(0,l/2,0)
    K=perspective.point(0,l/2,l)
    I.put_mark(0.2,0,"\( I\)",automatic_place=pspict)
    J.put_mark(0.2,180,"\( J\)",automatic_place=pspict)
    K.put_mark(0.2,45,"\( K\)",automatic_place=pspict)

    surface=Polygon(I,J,K)
    surface.parameters.filled()
    surface.parameters.fill.color="green"

    pspict.DrawGraphs(surface,I,J,K,cube)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
