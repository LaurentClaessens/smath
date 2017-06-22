# -*- coding: utf8 -*-
from phystricks import *
def FaussePerspectivewAwxAJ():
    pspict,fig = SinglePicture("FaussePerspectivewAwxAJ")
    pspict.dilatation(1)

    c=3
    perspective=ObliqueProjection(30,0.5)
    A=perspective.point(0,0,c)
    B=perspective.point(c,0,c)
    C=perspective.point(c,0,0)
    D=perspective.point(0,0,0)

    A.put_mark(0.2,135,"\( A\)",pspict=pspict)
    B.put_mark(0.2,45,"\( B\)",pspict=pspict)
    C.put_mark(0.2,-45,"\( C\)",pspict=pspict)
    D.put_mark(0.2,225,"\( D\)",pspict=pspict)

    carre=Polygon(A,B,C,D)
    carre.filled()
    K=Segment(A,B).midpoint()
    L=Segment(D,C).midpoint()
    J=perspective.point(c+1,0,c)
    K.parameters.symbol="x"
    L.parameters.symbol="x"
    J.parameters.symbol="x"
    K.put_mark(0.2,90,"\( K\)",pspict=pspict)
    L.put_mark(0.2,-90,"\( L\)",pspict=pspict)
    J.put_mark(0.2,90,"\( J\)",pspict=pspict)

    pspict.DrawGraphs(A,B,C,D,carre,K,L,J)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

