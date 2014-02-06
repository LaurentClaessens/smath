# -*- coding: utf8 -*-
from phystricks import *
def CFjmTFb():
    pspict,fig = SinglePicture("CFjmTFb")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),3,2,4)
    cube.put_vertex_mark(pspict)


    pspict.DrawGraphs(cube)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
