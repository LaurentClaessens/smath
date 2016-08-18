# -*- coding: utf8 -*-
from phystricks import *
def MWIPooDUJRIo():
    pspict,fig = SinglePicture("MWIPooDUJRIo")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(4,0)
    C=A+(-1,-2)
    D=B+(-1,-2.3)

    d1=Segment(A,B)
    d2=Segment(C,D)

    I=d1.midpoint()
    J=d2.midpoint()

    sec=Segment(I,J).dilatation(2)

    a1=Angle(B,I,sec.I)
    a2=Angle(sec.F,J,D)
    a1.put_mark(0.4,angle=None,text="\SI{34}{\degree}",pspict=pspict)
    a2.put_mark(0.4,angle=None,text="\SI{146}{\degree}",pspict=pspict)

    pspict.DrawGraphs(d1,d2,sec,a1,a2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
