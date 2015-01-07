# -*- coding: utf8 -*-
from phystricks import *
def MLZLooYDRsFl():
    pspict,fig = SinglePicture("MLZLooYDRsFl")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(1,-3)
    C=Point(0,-3)
    D=Point(1,0)

    s1=Segment(A,B)
    s2=Segment(C,D)
    
    I=Intersection(s1,s2)[0]

    angle=Angle(D,I,A)

    pspict.DrawGraphs(s1,s2,angle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
