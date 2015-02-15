# -*- coding: utf8 -*-
from phystricks import *
def GHKHooEnlVFf():
    pspict,fig = SinglePicture("GHKHooEnlVFf")
    pspict.dilatation_X(2)
    pspict.dilatation_Y(1)

    M=Point(0,0)
    N=Point(0,4)
    L=Point(1,0.5)
    K=Point(-2,3.5)

    d1=Segment(L,K)
    d2=Segment(M,N)

    pr1=0.5
    pr2=0.8
    A=d1.get_point_proportion(pr1)
    D=d2.get_point_proportion(pr1)
    O=Intersection(d1,d2)[0]

    O.put_mark(0.2,angle=None,text="\( O\)",automatic_place=(pspict,""))
    A.put_mark(0.2,angle=None,text="\( A\)",automatic_place=(pspict,""))
    D.put_mark(0.2,angle=None,text="\( D\)",automatic_place=(pspict,""))

    B=d1.get_point_proportion(pr2)
    C=d2.get_point_proportion(pr2)
    B.put_mark(0.2,angle=None,text="\( B\)",automatic_place=(pspict,""))
    C.put_mark(0.2,angle=None,text="\( C\)",automatic_place=(pspict,""))

    s1=Segment(B,C).dilatation(1.5)
    s2=Segment(A,D).dilatation(1.5)

    M.put_mark(0.2,angle=None,text="\( M\)",automatic_place=(pspict,""))
    N.put_mark(0.2,angle=None,text="\( N\)",automatic_place=(pspict,""))
    K.put_mark(0.2,angle=None,text="\( K\)",automatic_place=(pspict,""))
    L.put_mark(0.2,angle=None,text="\( L\)",automatic_place=(pspict,""))

    pspict.DrawGraphs(d1,d2,O,A,B,C,D,s1,s2,M,L,K,N)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
