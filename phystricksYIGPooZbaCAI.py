# -*- coding: utf8 -*-
from phystricks import *
def YIGPooZbaCAI():
    pspict,fig = SinglePicture("YIGPooZbaCAI")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=3
    K=Point(0,0)
    A=Point(l,0)
    M=Point(2*l,0)
    B=Point(3*l,0)
    L=Point(4*l,0)
    D=A+(0,-l)
    C=D+(2*l,0)

    rect=Polygon(A,B,C,D)
    lseg=[   Segment(K,A),Segment(A,M),Segment(M,B),Segment(B,L),Segment(A,D)   ]
    for seg in lseg:
        cod=seg.get_code( n=2,d=0.1,l=0.3,angle=45,pspict=pspict )
        pspict.DrawGraphs(cod)

    mesX=Segment(K,B).get_measure(-0.6,0.1,None,"\( x\)",pspict=pspict,position="corner")
    rect.put_mark(0.4,pspict=pspict)

    K.put_mark(0.2,90,"\( K\)",pspict=pspict)
    M.put_mark(0.2,90,"\( M\)",pspict=pspict)
    L.put_mark(0.2,90,"\( L\)",pspict=pspict)

    for p in [A,B,C,D]:
        p.parameters.symbol=""

    pspict.DrawGraphs(rect,mesX,lseg,K,M,L)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
