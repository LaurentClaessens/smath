# -*- coding: utf8 -*-
from phystricks import *
def EZTHooBttIaQ():
    pspict,fig = SinglePicture("EZTHooBttIaQ")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(0,-3)
    C=A+(1,0)
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

    #a1.put_mark(0.2,a1.advised_mark_angle,"\( a1\)",automatic_place=(pspict,"corner"))
    #a2.put_mark(0.2,a2.advised_mark_angle,"\( a2\)",automatic_place=(pspict,"corner"))
    #a3.put_mark(0.2,a3.advised_mark_angle,"\( a3\)",automatic_place=(pspict,"corner"))
    #a4.put_mark(0.2,a4.advised_mark_angle,"\( a4\)",automatic_place=(pspict,"corner"))

    #pspict.DrawGraphs(v1,v2,dig,a1,a2,a3,a4)
    pspict.DrawGraphs(v1,v2,dig,a2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
