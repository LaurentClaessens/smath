# -*- coding: utf8 -*-
from phystricks import *
def UOEOooLxhpSC():
    pspict,fig = SinglePicture("UOEOooLxhpSC")
    pspict.dilatation(1)

    cot=3
    A=Point(0,0)
    B=A+(cot,0)
    C=B+(0,-cot)
    D=A+(0,-cot)

    carre=Polygon(A,B,C,D)
    carre.put_mark(0.2,pspict=pspict)

    dig1=Segment(A,C)
    dig2=Segment(B,D)

    a1=Angle(D,A,C,r=0.7)
    a2=Angle(C,A,B)
    b1=Angle(A,B,D,r=0.7)
    b2=Angle(D,B,C)
    c1=Angle(B,C,A,r=0.7)
    c2=Angle(A,C,D)
    d1=Angle(C,D,B,r=0.7)
    d2=Angle(B,D,A)

    I=Intersection(dig1,dig2)[0]

    no_symbol(carre.vertices,I)

    a1.put_mark(0.2,angle=None,text="\( a_1\)",automatic_place=(pspict,""))
    a2.put_mark(0.2,angle=None,text="\( a_2\)",automatic_place=(pspict,""))
    b1.put_mark(0.2,angle=None,text="\( b_1\)",automatic_place=(pspict,""))
    b2.put_mark(0.2,angle=None,text="\( b_2\)",automatic_place=(pspict,""))
    c1.put_mark(0.2,angle=None,text="\( c_1\)",automatic_place=(pspict,""))
    c2.put_mark(0.2,angle=None,text="\( c_2\)",automatic_place=(pspict,""))
    d1.put_mark(0.2,angle=None,text="\( d_1\)",automatic_place=(pspict,""))
    d2.put_mark(0.2,angle=None,text="\( d_2\)",automatic_place=(pspict,""))

    I.put_mark(0.2,angle=90,text="\( I\)",automatic_place=(pspict,""))

    pspict.DrawGraphs(carre,a1,a2,b1,b2,c1,c2,d1,d2,dig1,dig2,I)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
