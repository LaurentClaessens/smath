# -*- coding: utf8 -*-
from phystricks import *
def RNTRooAXhubs():
    pspict,fig = SinglePicture("RNTRooAXhubs")
    pspict.dilatation(1)

    D=Point(0,0)
    E=Point(8,0)
    c1=Circle(D,12)
    c2=Circle(E,6)
    F=Intersection(c1,c2)[1]

    triangle=Polygon(D,E,F)
    triangle.put_mark(0.2,text_list=["\( D\)","\( E\)","\( F\)"],pspict=pspict)

    S=triangle.edges[2].midpoint()
    T=triangle.edges[1].midpoint()
    S.put_mark(0.2,S.advised_mark_angle,"\( S\)",automatic_place=(pspict,"corner"))
    T.put_mark(0.2,T.advised_mark_angle,"\( T\)",automatic_place=(pspict,"corner"))

    seg=Segment(S,T)

    pspict.DrawGraphs(S,T,triangle,seg)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
