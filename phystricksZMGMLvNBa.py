# -*- coding: utf8 -*-
from phystricks import *
def ZMGMLvNBa():
    pspict,fig = SinglePicture("ZMGMLvNBa")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    K=Point(-5,0)
    A=Point(0,3)
    B=Point(2,7)
    C=Point(6,5)
    D=Point(7,4)

    s1=Segment(K,A)
    s2=Segment(A,B)
    s3=Segment(B,C)
    s4=Segment(C,D)

    K.put_mark(0.2,90,"\( K\)",pspict=pspict,position="S")
    A.put_mark(0.2,-45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,90,"\( B\)",pspict=pspict,position="S")
    C.put_mark(0.2,45,"\( C\)",pspict=pspict,position="corner")
    D.put_mark(0.2,0,"\( D\)",pspict=pspict,position="W")

    pspict.DrawGraphs(K,A,B,C,D,s1,s2,s3,s4)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

