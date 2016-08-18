# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def figureFGgTGJA():
    pspict,fig = SinglePicture("figureFGgTGJA")
    pspict.dilatation(1)

    l=6
    h=2
    N=Point(0,h)
    M=Point(l,h)
    P=Point(l,0)
    B=Point(0,0)
    C=Point(l/2,h)
    A=Point(l/2,0)

    rect=Polygon(N,M,P,B)
    haut=Segment(C,A)
    d1=Segment(N,A)
    d2=Segment(C,B)
    d3=Segment(C,P)
    d4=Segment(M,A)

    N.put_mark(0.2,90+45,"\( N\)",pspict=pspict)
    B.put_mark(0.2,180+45,"\( B\)",pspict=pspict)
    A.put_mark(0.2,-90,"\( A\)",pspict=pspict)
    P.put_mark(0.2,-45,"\( P\)",pspict=pspict)
    M.put_mark(0.2,45,"\( M\)",pspict=pspict)
    C.put_mark(0.2,90,"\( C\)",pspict=pspict)

    pspict.DrawGraphs(N,M,P,B,C,A,rect,haut,d1,d2,d3,d4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
