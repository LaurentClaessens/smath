# -*- coding: utf8 -*-
from phystricks import *
def figureMYeLqLl():
    pspict,fig = SinglePicture("figureMYeLqLl")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(1,1)
    v=AffineVector(A,B)

    C=Point(-1,-2)+(-1,1)
    D=C+(-1,3)+(-1,1)
    w=AffineVector(C,D)

    K=Point(0,3)
    L=Point(-1,0)

    A.put_mark(0.2,0,"\( A\)",pspict=pspict)
    B.put_mark(0.2,0,"\( B\)",pspict=pspict)
    C.put_mark(0.2,0,"\( C\)",pspict=pspict)
    D.put_mark(0.2,0,"\( D\)",pspict=pspict)
    K.put_mark(0.2,0,"\( K\)",pspict=pspict)
    L.put_mark(0.2,0,"\( L\)",pspict=pspict)


    pspict.DrawGraphs(A,B,C,D,K,L)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
