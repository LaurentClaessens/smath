# -*- coding: utf8 -*-
from phystricks import *
def KUZZooNuCtFc():
    pspict,fig = SinglePicture("KUZZooNuCtFc")
    #pspict.dilatation_X(1)
    #pspict.dilatation_Y(1)
    pspict.dilatation(0.7)
    pspict.rotation(120)

    A=Point(0,0)
    C=Point(3,0)
    B=Point(C.x,4)

    trig1=Polygon(A,B,C)
    trig1.put_mark(0.2,pspict=pspict)

    K=trig1.edges[0].midpoint()
    L=trig1.edges[2].midpoint()
    K.put_mark(0.2,angle=None,added_angle=0,text="\( K\)",pspict=pspict)
    L.put_mark(0.2,angle=None,added_angle=0,text="\( L\)",pspict=pspict)

    trig1.edges[0].divide_in_two(n=2,d=0.1,l=0.2,angle=45,pspict=pspict)
    trig1.edges[2].divide_in_two(n=1,d=0.1,l=0.2,angle=45,pspict=pspict)

    #m1=Segment(A,K).get_mark(0.2,angle=None,added_angle=0,text="\SI{7.5}{\milli\meter}",pspict=pspict)
    #m2=Segment(L,A).get_mark(0.2,angle=None,added_angle=0,text="\SI{2.3}{\milli\meter}",pspict=pspict)
    #m3=Segment(K,L).get_mark(0.2,angle=None,added_angle=0,text="\SI{1,4}{\milli\meter}",pspict=pspict)

    midseg=Segment(K,L)
    
    no_symbol(trig1.vertices,K,L)

    pspict.DrawGraphs(trig1,K,L,midseg)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

