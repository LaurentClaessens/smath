# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def situation(pspict):
    l=2
    A=Point(0,0)
    B=Point(l,0)
    C=Point(l/3,-1)
    K=Point(-0.8,-1.7)

    v=AffineVector(A,B)
    D=C+v
    Kp=K+v

    parABDC=Polygon(A,B,D,C)
    parABKpK=Polygon(A,B,Kp,K)
    parABDC.edge.parameters.color="red"
    parABKpK.edge.parameters.color="blue"

    AB=Segment(A,B)
    AB.parameters.style="dashed"
    AB.parameters.color="red"

    seg1=Segment(C,K)
    seg2=Segment(D,Kp)
    seg1.parameters.style="dashed"
    seg2.parameters.style="dashed"

    A.put_mark(0.2,90,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,90,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,-45,"\( C\)",automatic_place=pspict)
    D.put_mark(0.2,-45,"\( D\)",automatic_place=pspict)
    K.put_mark(0.2,-90,"\( K\)",automatic_place=pspict)
    Kp.put_mark(0.2,-90,"\( K'\)",automatic_place=pspict)

    return parABDC,parABKpK,seg1,seg2,AB,A,B,C,D,K,Kp

def VectoParallItzteT():
    pspict,fig = SinglePicture("VectoParallItzteT")
    pspict.dilatation(3)

    graphes = situation(pspict)

    pspict.DrawGraphs(graphes)
    fig.conclude()
    fig.write_the_file()
