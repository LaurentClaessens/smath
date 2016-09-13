# -*- coding: utf8 -*-
from phystricks import *
def ThaleszlOKVq():
    pspict,fig = SinglePicture("ThaleszlOKVq")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,1)
    C=Point(4,-1)
    A.put_mark(0.2,90,"\( A\)",pspict=pspict)
    B.put_mark(0.2,90,"\( B\)",pspict=pspict)
    C.put_mark(0.2,90,"\( C\)",pspict=pspict)

    L=Segment(A,B).midpoint()
    L.put_mark(0.2,90,"\( L\)",pspict=pspict)
    K=Segment(A,C).midpoint()
    K.put_mark(0.2,90,"\( K\)",pspict=pspict)

    AB=Segment(A,B).dilatation(1.5)
    BC=Segment(B,C).dilatation(1.5)
    CA=Segment(C,A).dilatation(1.5)
    LK=Segment(L,K).dilatation(1.5)
    LK.parameters.color="red"


    pspict.DrawGraphs(AB,BC,CA,LK,A,B,C,L,K)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
