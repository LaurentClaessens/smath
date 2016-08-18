# -*- coding: utf8 -*-
from phystricks import *
def YDTGooZGkkei():
    pspict,fig = SinglePicture("YDTGooZGkkei")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    K=Point(0,0)
    M=Point(4,0)
    L=Point(M.x+2,3)

    trig=Polygon(K,L,M).rotation(20)
    trig.put_mark(0.3,points_names="BAC",pspict=pspict)

    K=trig.vertices[0]
    L=trig.vertices[1]
    M=trig.vertices[2]

    R=Segment(K,M).midpoint()
    S=Segment(K,L).midpoint()

    m1=Segment(L,R)
    m2=Segment(R,S)

    trig.edges[0].divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspict)
    trig.edges[2].divide_in_two(n=1,d=0.1,l=0.3,angle=45,pspict=pspict)

    R.put_mark(0.2,angle=None,added_angle=180,text="\( T\)",pspict=pspict)
    S.put_mark(0.2,angle=None,added_angle=0,text="\( S\)",pspict=pspict)

    no_symbol(trig.vertices)

    pspict.DrawGraphs(trig,R,S,m1,m2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
