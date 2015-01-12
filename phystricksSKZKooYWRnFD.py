# -*- coding: utf8 -*-
from phystricks import *
def SKZKooYWRnFD():
    pspict,fig = SinglePicture("SKZKooYWRnFD")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    vect=(0,-1)
    A=Point(0,0)
    B=Point(3,1)
    s1=Segment(A,B)
    s2=s1+vect

    I=s1.get_point_proportion(0.3)
    J=s2.get_point_proportion(0.6)
    s3=Segment(I,J).dilatation(1.7)

    pspict.DrawGraphs(s1,s2,s3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
