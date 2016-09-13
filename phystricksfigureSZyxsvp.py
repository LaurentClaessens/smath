# -*- coding: utf8 -*-
from phystricks import *
def figureSZyxsvp():
    pspict,fig = SinglePicture("figureSZyxsvp")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(4,3)
    K=Segment(A,B).midpoint()
    I=K.projection(pspict.axes.single_axeX)
    J=B.projection(pspict.axes.single_axeX)

    A.put_mark(0.2,90+45,"\( A\)",pspict=pspict)
    B.put_mark(0.2,45,"\( B\)",pspict=pspict)
    K.put_mark(0.2,90+45,"\( K\)",pspict=pspict)
    I.put_mark(0.2,-90,"\( I\)",pspict=pspict)
    J.put_mark(0.2,-90,"\( J\)",pspict=pspict)

    v1=Segment(K,I)
    v2=Segment(B,J)
    v1.parameters.style="dashed"
    v2.parameters.style="dashed"
    AB=Segment(A,B)

    pspict.DrawGraphs(A,B,K,I,J,v1,v2,AB)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
