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
    D=C.translate(v)
    Kp=K.translate(v)

    parABDC=Polygon(A,B,D,C)
    parABKpK=Polygon(A,B,Kp,K)
    parABDC.edge_model.parameters.color="red"
    parABKpK.edge_model.parameters.color="blue"

    AB=Segment(A,B)
    AB.parameters.style="dashed"
    AB.parameters.color="red"

    seg1=Segment(C,K)
    seg2=Segment(D,Kp)
    seg1.parameters.style="dashed"
    seg2.parameters.style="dashed"

    A.put_mark(0.2,90,"\( A\)",pspict=pspict)
    B.put_mark(0.2,90,"\( B\)",pspict=pspict)
    C.put_mark(0.2,-45,"\( C\)",pspict=pspict)
    D.put_mark(0.2,-45,"\( D\)",pspict=pspict)
    K.put_mark(0.2,-90,"\( K\)",pspict=pspict)
    Kp.put_mark(0.2,-90,"\( K'\)",pspict=pspict)

    return parABDC,parABKpK,seg1,seg2,AB,A,B,C,D,K,Kp

def VectoParallItzteT():
    pspict,fig = SinglePicture("VectoParallItzteT")
    pspict.dilatation(3)

    graphes = situation(pspict)

    pspict.DrawGraphs(graphes)
    fig.conclude()
    fig.write_the_file()
