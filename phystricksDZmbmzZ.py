# -*- coding: utf8 -*-
from phystricks import *
def DZmbmzZ():
    pspict,fig = SinglePicture("DZmbmzZ")
    pspict.dilatation(1)

    A=Point(3,4)
    B=Point(0,0)
    C=Point(6,0)

    BC=Segment(B,C)

    triangle=Polygon(A,B,C)
    A.put_mark(0.2,90,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,180,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,0,"\( C\)",automatic_place=pspict)

    H=A.projection(BC)
    H.put_mark(0.2,-90,"\( H\)",automatic_place=pspict)
    AH=Segment(A,H)
    AH.put_mark(0.2,0,"\( 4\)",automatic_place=pspict)

    a1=Angle(B,A,H)
    a2=Angle(H,A,C)
    a1.put_mark(0.2,a1.advised_mark_angle,"\( 45\)",automatic_place=pspict)
    a2.put_mark(0.2,a2.advised_mark_angle,"\( 60\)",automatic_place=pspict)

    pspict.DrawGraphs(triangle,A,B,C,AH,H,a1,a2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
