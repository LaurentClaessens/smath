# -*- coding: utf8 -*-
from phystricks import *
def DansRectangleGPEkJc():
    pspict,fig = SinglePicture("DansRectangleGPEkJc")
    pspict.dilatation(0.5)

    l=7
    h=3

    A=Point(0,h)
    B=Point(l,h)
    C=Point(l,0)
    D=Point(0,0)
    J=Point(l-h,0)
    I=Point(l-h,h)
    A.put_mark(0.2,135,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,45,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,-45,"\( C\)",automatic_place=pspict)
    D.put_mark(0.2,180+45,"\( D\)",automatic_place=pspict)
    I.put_mark(0.2,90,"\( I\)",automatic_place=pspict)
    J.put_mark(0.2,-90,"\( J\)",automatic_place=pspict)
    rect=Polygon(A,B,C,D)
    rect.parameters.filled()
    s=Segment(B,J)
    t=Segment(J,I)
    t.parameters.style="dashed"
    angle=Angle(I,B,J,r=0.7)
    angle.parameters.color="red"

    angle.put_mark(0.3,angle.advised_mark_angle,"\unit{45}{\degree}",automatic_place=pspict)

    pspict.specific_needs="\usepackage{SIunits}"
    pspict.DrawGraphs(rect,A,B,C,D,I,J,s,t,angle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
