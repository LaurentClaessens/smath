# -*- coding: utf8 -*-
from phystricks import *
def CubeLigneTriangleHFMrVU():
    pspict,fig = SinglePicture("CubeLigneTriangleHFMrVU")
    pspict.dilatation(1)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    surface=Polygon(cube.D,cube.B,cube.F)
    surface.filled()
    surface.fill_parameters.color="green"

    pspict.DrawGraphs(surface,cube)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
