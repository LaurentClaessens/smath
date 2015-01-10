# -*- coding: utf8 -*-
from phystricks import *
def MLZLooYDRsFl():
    pspict,fig = SinglePicture("MLZLooYDRsFl")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=1.5
    A=Point(0,0)
    B=Point(l,-3)
    C=Point(0,-3)
    D=Point(l,0)

    s1=Segment(A,B)
    s2=Segment(C,D)
    
    I=Intersection(s1,s2)[0]

    angle=Angle(D,I,A)
    angle.put_mark(0.4,angle.advised_mark_angle,"\small\SI{30}{\degree}",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(s1,s2,angle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
