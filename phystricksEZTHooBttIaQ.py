# -*- coding: utf8 -*-
from phystricks import *
def EZTHooBttIaQ():
    pspict,fig = SinglePicture("EZTHooBttIaQ")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(0,-3)
    C=A+(1.5,0)
    D=B+C-A

    v1=Segment(A,B)
    v2=Segment(C,D)

    p=0.1
    K=v1.get_point_proportion(p)
    L=v2.get_point_proportion(1-p)
    dig=Segment(K,L)

    a1=Angle(L,K,A)
    a2=Angle(B,K,L)
    a3=Angle(C,L,K)
    a4=Angle(K,L,D)

    a2.put_mark(0.4,None,"\small\SI{45}{\degree}",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(v1,v2,dig,a2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
