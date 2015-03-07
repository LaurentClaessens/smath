# -*- coding: utf8 -*-
from phystricks import *
def LOPLooZJmTuk():
    pspict,fig = SinglePicture("LOPLooZJmTuk")
    pspict.dilatation(0.63)

    l=3
    h=4
    perspective=ObliqueProjection(30,0.5)
    G=perspective.point(0,0,0)
    F=perspective.point(0,0,4)
    E=perspective.point(5,0,0)
    S=perspective.point(0,6,0)

    trig=Polygon(S,G,E)
    trig.put_mark(0.2,points_names="GFE",pspict=pspict)


    pspict.DrawGraphs(trig)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
