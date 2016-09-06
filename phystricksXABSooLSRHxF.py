# -*- coding: utf8 -*-
from phystricks import *


def PDNJooMoHgCM():
    pspict,fig = SinglePicture("PDNJooMoHgCM")
    pspict.dilatation(0.40)

    l=3
    h=4
    perspective=ObliqueProjection(90+30,0.5)
    R=perspective.point(0,0,0)
    U=perspective.point(7,0,0)
    S=perspective.point(7,5,0)
    T=perspective.point(7,0,3)

    trig=Polygon(R,S,U)
    trig.put_mark(0.2,points_names="RSU",pspict=pspict)
    T.put_mark(0.2,angle=90+45,text="\( T\)",pspict=pspict)

    for ver in [S,R,U]:
        seg=Segment(T,ver)
        seg.parameters.style="dashed"
        pspict.DrawGraphs(seg)

    no_symbol(R,S,T,U)


    pspict.DrawGraphs(trig,T)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

l1=7
l2=3
h=5

def EIHJooJrGgmN():
    pspict,fig = SinglePicture("EIHJooJrGgmN")
    pspict.dilatation(0.40)


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


def XABSooLSRHxF():
    PDNJooMoHgCM()
    EIHJooJrGgmN()
