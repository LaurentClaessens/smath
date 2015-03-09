# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def NFCHooAFFYPx():
    pspict,fig = SinglePicture("NFCHooAFFYPx")
    pspict.dilatation(0.68)


    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspict)

    I=perspective.point(l/2,l/2,l/2)
    I.put_mark(0.2,angle=180,text="\( I\)",automatic_place=(pspict,""))

    segs=[   Segment(x,I) for x in [cube.B,cube.F,cube.G,cube.C]    ]
    for se in segs:
        se.parameters.style='dashed'

    no_symbol(I)

    pspict.DrawGraphs(cube,segs,I)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
