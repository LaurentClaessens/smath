# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def SurfaceCubeXlLEEy():
    pspict,fig = SinglePicture("SurfaceCubeXlLEEy")
    pspict.dilatation(0.7)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    I=perspective.point(l/2,l/2,0)
    J=perspective.point(0,l/2,0)
    K=perspective.point(0,l/2,l)
    I.put_mark(0.2,0,"\( I\)",pspict=pspict)
    J.put_mark(0.2,180,"\( J\)",pspict=pspict)
    K.put_mark(0.2,45,"\( K\)",pspict=pspict)

    surface=Polygon(I,J,K)
    surface.filled()
    surface.fill_parameters.color="green"

    pspict.DrawGraphs(surface,I,J,K,cube)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
