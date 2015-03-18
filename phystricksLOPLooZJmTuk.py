# -*- coding: utf8 -*-
from phystricks import *
def LOPLooZJmTuk():
    pspict,fig = SinglePicture("LOPLooZJmTuk")
    pspict.dilatation(0.40)

    l=3
    h=4
    perspective=ObliqueProjection(30,0.5)
    M=perspective.point(0,0,0)
    K=perspective.point(0,0,4)
    L=perspective.point(5,0,0)
    S=perspective.point(0,6,0)

    trig=Polygon(S,M,L)
    trig.put_mark(0.2,points_names="SML",pspict=pspict)
    K.put_mark(0.2,angle=45,text="\( K\)",automatic_place=(pspict,""))

    SK=Segment(S,K)
    MK=Segment(M,K)
    LK=Segment(L,K)

    for s in [SK,MK,LK]:
        s.parameters.style='dashed'

    no_symbol(L,K,M,S)


    pspict.DrawGraphs(trig,SK,MK,LK,K)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
