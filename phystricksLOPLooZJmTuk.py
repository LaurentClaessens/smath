# -*- coding: utf8 -*-
from phystricks import *
def LOPLooZJmTuk():
    pspict,fig = SinglePicture("LOPLooZJmTuk")
    pspict.dilatation(0.43)

    l=3
    h=4
    perspective=ObliqueProjection(30,0.5)
    G=perspective.point(0,0,0)
    K=perspective.point(0,0,4)
    L=perspective.point(5,0,0)
    S=perspective.point(0,6,0)

    trig=Polygon(S,G,L)
    trig.put_mark(0.2,points_names="SGL",pspict=pspict)
    K.put_mark(0.2,angle=45,text="\( K\)",automatic_place=(pspict,""))

    SK=Segment(S,K)
    GK=Segment(G,K)
    LK=Segment(L,K)

    for s in [SK,GK,LK]:
        s.parameters.style='dashed'

    no_symbol(L,K,G,S)


    pspict.DrawGraphs(trig,SK,GK,LK,K)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
