# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def DWHNooSCJJNE():
    pspict,fig = SinglePicture("DWHNooSCJJNE")
    pspict.dilatation(1)

    l=8
    h=5
    n=5
    lc=l/n

    A=Point(0,0)
    B=A+(0,h)
    C=B+(l,0)
    D=A+C-B

    rect=Polygon(A,B,C,D)
    rect.make_edges_independent()
    rect.edges[0].parameters.linewidth=2
    rect.edges[2].parameters.linewidth=2
    K=[B+(i*lc,0) for i in range(0,n+1) ]
    L=[A+(i*lc,0) for i in range(0,n+1) ]
    for i in range(1,n+1):
        seg=Segment(  K[i],L[i] )
        seg.parameters.style="dashed"
        cod1=Segment(  K[i],K[i-1]  ).get_code(n=2,d=0.1,l=0.3,pspict=pspict)
        cod2=Segment(  L[i],L[i-1]  ).get_code(n=2,d=0.1,l=0.3,pspict=pspict)
        pspict.DrawGraphs(seg,cod1,cod2)

    pspict.comment="The two vertical lines have larges width"
    pspict.DrawGraphs(rect)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
