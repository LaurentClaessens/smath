# -*- coding: utf8 -*-
from phystricks import *
def ZUVLooJNWbPB():
    pspict,fig = SinglePicture("ZUVLooJNWbPB")
    pspict.dilatation(1)

    A=Point(0,0)
    B=A+(3,0)
    C=A+(1,2)
    D=A+C-B

    parall=Polygon(A,B,C,D)
    parall.put_mark(0.2,pspict=pspict)
    diag1=Segment(A,C)

    no_symbol(parall.vertices)

    a1=Angle(C,A,D,r=0.3)
    a2=Angle(B,A,C)
    c1=Angle(D,C,A,)
    c2=Angle(A,C,B,r=0.3)
    d1=Angle(A,D,C)
    b1=Angle(C,B,A)

    a1.put_mark(0.2,angle=None,text="\( a_1\)",automatic_place=(pspict,""))
    a2.put_mark(0.2,angle=None,text="\( a_2\)",automatic_place=(pspict,""))
    c1.put_mark(0.2,angle=None,text="\( c_1\)",automatic_place=(pspict,""))
    c2.put_mark(0.2,angle=None,text="\( c_2\)",automatic_place=(pspict,""))

    pspict.DrawGraphs(parall,diag1,a1,a2,b1,c1,c2,d1)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

