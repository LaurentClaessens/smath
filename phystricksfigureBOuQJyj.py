# -*- coding: utf8 -*-
from phystricks import *
def figureBOuQJyj():
    pspict,fig = SinglePicture("figureBOuQJyj")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,1)
    C=Point(5,-1)
    D=Point(0,-2)

    quad=Polygon(A,B,C,D)
    I=Segment(A,B).center()
    J=Segment(B,C).center()
    K=Segment(C,D).center()
    L=Segment(D,A).center()

    A.put_mark(0.2,135,"\( A\)",pspict=pspict)
    B.put_mark(0.2,45,"\( B\)",pspict=pspict)
    C.put_mark(0.2,0,"\( C\)",pspict=pspict)
    D.put_mark(0.2,180+45,"\( D\)",pspict=pspict)
    I.put_mark(0.2,90,"\( I\)",pspict=pspict)
    J.put_mark(0.2,0,"\( J\)",pspict=pspict)
    K.put_mark(0.2,-70,"\( K\)",pspict=pspict)
    L.put_mark(0.2,180,"\( L\)",pspict=pspict)

    dig=Segment(A,C)
    dig.parameters.style="dashed"
    dig.parameters.color="blue"

    paral=Polygon(I,J,K,L)

    pspict.DrawGraphs(quad,A,B,C,D,I,J,K,L,paral,dig)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
