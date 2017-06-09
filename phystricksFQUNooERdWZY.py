# -*- coding: utf8 -*-
from phystricks import *
def FQUNooERdWZY():
    pspict,fig = SinglePicture("FQUNooERdWZY")
    pspict.dilatation(0.7)

    vect=(1,0)
    A=Point(0,0)
    B=Point(0,3)
    s1=Segment(A,B)
    s2=s1.translate(vect)

    I=s1.get_point_proportion(0.2)
    J=s2.get_point_proportion(0.65)
    s3=Segment(I,J).dilatation(1.7)

    pspict.DrawGraphs(s1,s2,s3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
