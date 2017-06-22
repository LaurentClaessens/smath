# -*- coding: utf8 -*-
from phystricks import *
def PMVPooKtUXux():
    pspict,fig = SinglePicture("PMVPooKtUXux")
    pspict.dilatation(0.5)

    S=Point(0,0)
    T=Point(6,0)
    A=Point(5,1)
    B=Point(5,-1)

    AB=Segment(A,B)
    loz=Polygon(S,A,T,B)
    loz.edges_parameters.style="dashed"

    loz.put_mark(0.2,text_list=[  "\( S\)","\( A\)","\( T\)","\( B\)"  ],pspict=pspict)

    loz.edges[0].put_code(n=1,d=0.1,angle=-45,l=0.4,pspict=pspict)
    loz.edges[3].put_code(n=1,d=0.1,l=0.4,pspict=pspict)

    loz.edges[1].put_code(n=2,d=0.1,angle=-45,l=0.4,pspict=pspict)
    loz.edges[2].put_code(n=2,d=0.1,l=0.4,pspict=pspict)

    pspict.DrawGraphs(A,B,S,T,AB,loz)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
