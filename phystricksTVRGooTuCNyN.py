# -*- coding: utf8 -*-
from phystricks import *
def TVRGooTuCNyN():
    pspict,fig = SinglePicture("TVRGooTuCNyN")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(3,3)
    I=Segment(A,B).midpoint()

    v=(-1,2)
    s1=Segment(A,B).dilatation(1.3)
    C=A+v
    D=B+v
    s2=Segment(C,D).dilatation(1.3)
    P=I+(-2,1)
    J=Intersection( s2,Segment(I,P) )[0]
    t=Segment(I,J).dilatation(1.7)

    a1=Angle( t.I,I,B )
    a2=Angle(C,J,I)
    a1.put_mark(0.4,None,"\SI{28}{\degree}",automatic_place=(pspict,""))
    a2.put_mark(0.4,None,"\SI{132}{\degree}",automatic_place=(pspict,""))


    pspict.DrawGraphs(s1,s2,t,a1,a2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
