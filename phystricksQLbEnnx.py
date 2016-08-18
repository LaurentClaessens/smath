# -*- coding: utf8 -*-
from phystricks import *
def QLbEnnx():
    pspict,fig = SinglePicture("QLbEnnx")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)



    l=3
    h=4
    dilatation=1.5
    perspective=ObliqueProjection(30,0.5)
    A=perspective.point(1,3,0.5)
    B=perspective.point(0,0,0)
    C=perspective.point(2,0,-2)
    D=perspective.point(3,0,1)

    AB=Segment(A,B)
    BC=Segment(B,C)
    CD=Segment(C,D)
    BD=Segment(B,D)
    AC=Segment(A,C)
    AD=Segment(A,D)

    BD.parameters.style='dashed'

    A.put_mark(0.2,90,"\( A\)",pspict=pspict)
    B.put_mark(0.2,180,"\( B\)",pspict=pspict)
    C.put_mark(0.2,-90,"\( C\)",pspict=pspict)
    D.put_mark(0.2,-90,"\( D\)",pspict=pspict)

    J=AD.get_point_proportion(0.3)
    I=BC.get_point_proportion(0.7)

    I.put_mark(0.2,200,"\( I\)",pspict=pspict)
    J.put_mark(0.2,90,"\( J\)",pspict=pspict)

    pspict.DrawGraphs(A,B,C,D,I,J,AB,AC,AD,BC,CD,BD)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
