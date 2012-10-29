# -*- coding: utf8 -*-
from phystricks import *
def ThaleszlOKVq():
    pspict,fig = SinglePicture("ThaleszlOKVq")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,1)
    C=Point(4,-1)
    A.put_mark(0.2,90,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,90,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,90,"\( C\)",automatic_place=pspict)

    L=Segment(A,B).center()
    L.put_mark(0.2,90,"\( L\)",automatic_place=pspict)
    K=Segment(A,C).center()
    K.put_mark(0.2,90,"\( K\)",automatic_place=pspict)

    AB=Segment(A,B).dilatation(1.5)
    BC=Segment(B,C).dilatation(1.5)
    CA=Segment(C,A).dilatation(1.5)
    LK=Segment(L,K).dilatation(1.5)
    LK.parameters.color="red"


    pspict.DrawGraphs(AB,BC,CA,LK,A,B,C,L,K)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
