# -*- coding: utf8 -*-
from phystricks import *
def HHOooQUedri():
    pspict,fig = SinglePicture("HHOooQUedri")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    A=Point(0,0)
    B=Point(2,1)
    C=Point(1,4)

    triangle=Polygon(A,B,C)
    AB=Segment(A,B)
    AB.put_mark(0.2,AB.advised_mark_angle(pspict)+180,"\( 4\)",pspict=pspict,position="corner")
    AC=Segment(A,C)
    AC.put_mark(0.2,AC.advised_mark_angle(pspict),"\( 13\)",pspict=pspict,position="corner")
    BC=Segment(B,C)
    BC.put_mark(0.2,BC.advised_mark_angle(pspict)+180,"\( 7\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(triangle,AB,AC,BC)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
