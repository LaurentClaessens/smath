# -*- coding: utf8 -*-
from phystricks import *
def OKTXHoc():
    pspict,fig = SinglePicture("OKTXHoc")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    pspict.DrawGraphs(cube)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
