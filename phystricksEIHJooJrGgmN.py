# -*- coding: utf8 -*-
from phystricks import *

def EIHJooJrGgmN():
    pspict,fig = SinglePicture("EIHJooJrGgmN")
    pspict.dilatation(0.40)

    l1=7
    l2=3
    h=5

    R=Point(0,0)
    U=Point(l1,0)
    T=Point(U.x,l2)
    S1=U+(h,0)
    S2=U+(0,-h)
    trig=Polygon(R,T,U)
    trig.put_mark(0.2,points_names="RTU",pspict=pspict)

    d1=Segment(S1,T)
    d2=Segment(S2,R)

    cer1=Circle(   T,  d1.length )
    cer2=Circle(R,d2.length)
    S3=Intersection(cer1,cer2)[0]

    d3=Segment(R,S3)
    c1=Segment(U,S1)
    c2=Segment(U,S2)
    c3=Segment(T,S3)

    no_symbol(trig.vertices, S1,S2,S3)

    pspict.DrawGraphs(trig,S1,S2,S3,d1,d2,d3,c1,c2,c3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
