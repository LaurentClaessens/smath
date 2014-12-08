# -*- coding: utf8 -*-
from phystricks import *
def XFMTooSCJlTh():
    pspict,fig = SinglePicture("XFMTooSCJlTh")
    pspict.dilatation(1)

    alpha=30
    A=Point(0,9)
    cer=Circle(A,4)
    B=cer.get_point(-90-alpha)
    C=cer.get_point(-90+alpha)

    s1=Segment(A,B)
    s2=Segment(A,C)

    E=s1.proportion(0.3)
    F=s2.proportion(0.3)

    s3=Segment(E,F)

    pspict.DrawGraphs(s1,s2,s3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

