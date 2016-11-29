# -*- coding: utf8 -*-
from phystricks import *
def SYKMooKLBCXR():
    pspict,fig = SinglePicture("SYKMooKLBCXR")
    pspict.dilatation(1)

    K=Point(0,0)
    L=Point(4,0)
    M=Point(3,2)

    trig=Polygon(K,L,M)
    trig.put_mark(0.2,text_list=["\( K\)","\( L\)","\( M\)"],pspict=pspict)

    S=Segment(K,M).midpoint()
    T=Segment(K,L).midpoint()
    drm=Segment(S,T)

    drm.put_mark(0.1,drm.advised_mark_angle(pspict),"\( 8\)",pspict=pspict)
    trig.edges[1].put_mark(0.2,trig.edges[1].advised_mark_angle(pspict),added_angle=180,text="\( 16\)",pspict=pspict)

    S.put_mark(0.2,S.advised_mark_angle(pspict),"\( S\)",pspict=pspict)
    T.put_mark(0.2,-90,"\( T\)",pspict=pspict)

    for x in [K,L,M,S,T]:
        x.parameters.symbol=""


    pspict.comment="The mark of 'S' is orthogonal to (KM) and the one of 'T' is below the point (angle=-90)"
    pspict.DrawGraphs(trig,drm,S,T)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
