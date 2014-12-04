# -*- coding: utf8 -*-
from phystricks import *
def JJHQooEkspEV():
    pspict,fig = SinglePicture("JJHQooEkspEV")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    S=Point(0,0)
    T=Point(3,-2)
    R=Point(3,4)

    triangle=Polygon(S,T,R)
    triangle.put_mark(0.2,text_list=['\( S\)',"\( T\)","\( R\)"],pspict=pspict)

    M=triangle.edges[2].midpoint()
    M.put_mark(0.2,M.advised_mark_angle+180,"\( M\)",automatic_place=(pspict,"corner"))
    O=triangle.edges[0].midpoint()
    O.put_mark(0.2,O.advised_mark_angle+180,"\( O\)",automatic_place=(pspict,"corner"))

    seg=Segment(M,O)
    triangle.edges[2].divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspict)

    pspict.DrawGraphs(triangle,seg,M,O)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
