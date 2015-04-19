# -*- coding: utf8 -*-
from phystricks import *
def XABSooLSRHxF():
    pspict,fig = SinglePicture("XABSooLSRHxF")
    pspict.dilatation(0.40)

    l=3
    h=4
    perspective=ObliqueProjection(90+30,0.5)
    R=perspective.point(0,0,0)
    U=perspective.point(7,0,0)
    S=perspective.point(7,5,0)
    T=perspective.point(7,0,3)

    trig=Polygon(R,S,U)
    trig.put_mark(0.2,points_names="RSU",pspict=pspict)
    T.put_mark(0.2,angle=90+45,text="\( T\)",automatic_place=(pspict,""))

    for ver in [S,R,U]:
        seg=Segment(T,ver)
        seg.parameters.style="dashed"
        pspict.DrawGraphs(seg)

    no_symbol(R,S,T,U)


    pspict.DrawGraphs(trig,T)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
