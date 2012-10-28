# -*- coding: utf8 -*-
from phystricks import *
def RectanglegHuBZs():
    pspict,fig = SinglePicture("RectanglegHuBZs")
    pspict.dilatation(0.3)

    A=Point(0,0)
    B=Point(8,0)
    C=Point(8,15)

    AB=Segment(A,B)
    BC=Segment(B,C)
    CA=Segment(C,A)

    A.put_mark(0.2,225,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,-45,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,90,"\( C\)",automatic_place=pspict)
    AB.put_mark(0.2,-90,"\( 8\)",automatic_place=pspict)
    BC.put_mark(0.2,0,"\( x\)",automatic_place=pspict)
    CA.put_mark(0.2,CA.advised_mark_angle()+180,"\( 17\)",automatic_place=pspict)

    pspict.DrawGraphs(A,B,C,AB,BC,CA)
    fig.conclude()
    fig.write_the_file()
