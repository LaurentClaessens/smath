# -*- coding: utf8 -*-
from phystricks import *
def AILoxBg():
    pspict,fig = SinglePicture("AILoxBg")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    A=Point(3,3)
    B=Point(0,3)
    C=Point(-3,0)
    D=Point(0,-3)
    E=Point(3,0)
    F=Point(3,-3)
    O=Point(0,0)

    A.put_mark(0.2,45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,text="\( B\)",pspict=pspict,position="S")
    C.put_mark(0.2,text="\( C\)",pspict=pspict,position="E")
    D.put_mark(0.2,text="\( D\)",pspict=pspict,position="N")
    E.put_mark(0.2,text="\( E\)",pspict=pspict,position="W")
    F.put_mark(0.2,-45,"\( F\)",pspict=pspict,position="corner")
    O.put_mark(0.2,45,"\( O\)",pspict=pspict,position="corner")

    s1=Segment(C,B)
    s2=Segment(B,A)
    s3=Segment(A,F)
    s4=Segment(D,C)
    s5=Segment(F,D)
    s6=Segment(B,D)
    s7=Segment(C,E)

    pspict.DrawGraphs(A,B,C,D,E,F,O,s1,s2,s3,s4,s5,s6,s7)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

