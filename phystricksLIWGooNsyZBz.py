# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def LIWGooNsyZBz():
    pspict,fig = SinglePicture("LIWGooNsyZBz")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(2)

    l=3

    A=Point(0,0)
    B=Point(l,0)
    C=Point(B.x,l)
    D=Point(A.x,C.y)

    carre=Polygon(A,B,C,D)
    carre.put_mark(0.4,pspict=pspict)

    ex=l/3
    E=Point(ex,tan(  50*pi/180 )*ex)

    L=Point(ex*2,0)
    EL=Segment(E,L)
    AE=Segment(A,E)
    K=Intersection(AE,carre.edges[2])[0]

    AK=Segment(A,K)

    L.put_mark(0.4,angle=-90,added_angle=0,text="\( L\)",automatic_place=(pspict,""))
    K.put_mark(0.4,angle=90,added_angle=0,text="\( K\)",automatic_place=(pspict,""))
    E.put_mark(0.4,angle=90+45,added_angle=0,text="\( E\)",automatic_place=(pspict,""))

    an=AngleAOB(A,E,L)
    an.put_mark(0.2,angle=None,added_angle=0,text="\SI{80}{\degree}",automatic_place=(pspict,""))

    put_equal_lengths_code(AE,EL,n=2,d=0.1,l=0.3,angle=45,pspict=pspict)

    no_symbol(carre.vertices,K,L,E)
    pspict.DrawGraphs(carre,EL,AK,AE,L,K,an,E)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

