# -*- coding: utf8 -*-
from phystricks import *
def PerpSegqrbMBZ():
    pspict,fig = SinglePicture("PerpSegqrbMBZ")
    pspict.dilatation(1)

    P=Point(0,2)
    Q=Point(1,0)
    I=Point(2,1)

    PQ=Segment(P,Q)
    cercle=Circle(I,2.5)
    cercle.parameters.style="dashed"
    cercle.parameters.color="blue"

    pts=Intersection(cercle,PQ)
    A=pts[0]
    B=pts[1]
    seg=Segment(A,B).dilatation(1.3)
    M=I.projection(seg)

    A.put_mark(0.2,0,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,225,"\( B\)",automatic_place=pspict)
    I.put_mark(0.2,90,"\( I\)",automatic_place=pspict)
    M.put_mark(0.2,-20,"\( M\)",automatic_place=pspict)

    IM=Segment(I,M).dilatation(1.3)
    IM.parameters.color="red"
    IM.parameters.style="dashed"

    pspict.DrawGraphs(cercle,seg,I,IM,A,B,M)
    fig.conclude()
    fig.write_the_file()

