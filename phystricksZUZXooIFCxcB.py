# -*- coding: utf8 -*-
from phystricks import *
def ZUZXooIFCxcB():
    pspict,fig = SinglePicture("ZUZXooIFCxcB")
    pspict.dilatation(0.73)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    #edges=[  Segment(x,cube.F) for x in [cube.H,cube.G,cube.C,cube.D]  ]
    #for s in edges:
    #    s.parameters.style="dashed"
    #edges[2].parameters.style=""

    pspict.DrawGraphs(cube)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
