# -*- coding: utf8 -*-
from phystricks import *
def BKWooKbAHbD():
    pspict,fig = SinglePicture("BKWooKbAHbD")
    pspict.dilatation(0.7)

    A=Point(0,0)
    B=Point(4,1)
    AB=Segment(A,B)

    r=AB.length()*0.75
    angle=AB.angle()*degree

    A.put_mark(0.2,AB.advised_mark_angle(pspict),"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,AB.advised_mark_angle(pspict),"\( B\)",automatic_place=(pspict,"corner"))

    c1=Circle(A,r).graph(angle+90*degree,angle-90*degree)
    c2=Circle(B,r).graph(angle+90*degree,angle+270*degree)

    c1.parameters.style="dashed"
    c2.parameters.style="dashed"

    inter=Intersection(c1,c2)
    P=inter[0]
    Q=inter[1]

    media=Segment(P,Q).dilatation(1.5)

    pspict.DrawGraphs(A,B,AB,c1,c2,P,Q,media)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
