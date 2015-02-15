# -*- coding: utf8 -*-
from phystricks import *
def DIPLooHILUUs():
    pspict,fig = SinglePicture("DIPLooHILUUs")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    T=Point(0,0)
    O=Point(5,0)
    R=Point(4,4)
    
    triangle=Polygon(T,O,R)
    triangle.put_mark(0.2,text_list=["\( T\)","\( O\)","\( R\)"],pspict=pspict)
    triangle.edges[1].divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspict)

    M=triangle.edges[1].midpoint()

    segi=triangle.edges[2].parallel_trough(M)
    N=Intersection(segi,triangle.edges[0])[0]
    
    seg=Segment(M,N).dilatation(1.5)

    M.put_mark(0.2,None,"\( M\)",automatic_place=(pspict,"corner"))
    N.put_mark(0.2,-45,"\( N\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(triangle,N,M,seg)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

