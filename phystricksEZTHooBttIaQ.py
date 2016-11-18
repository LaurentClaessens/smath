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

    a1=AngleAOB(L,K,A)
    a2=AngleAOB(B,K,L)
    a3=AngleAOB(C,L,K)
    a4=AngleAOB(K,L,D)

    a2.put_mark(text="\small\SI{45}{\degree}",pspict=pspict)

    pspict.DrawGraphs(v1,v2,dig,a2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
