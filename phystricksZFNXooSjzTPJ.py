# -*- coding: utf8 -*-
from phystricks import *
def ZFNXooSjzTPJ():
    pspict,fig = SinglePicture("ZFNXooSjzTPJ")
    pspict.dilatation(0.7)

    E=Point(0,0)
    F=Point(0,3)
    G=Point(4,2)

    triangle=Polygon(E,F,G)
    triangle.put_mark(0.2,[ "\( E\)","\( F\)","\( G\)" ],pspict=pspict)
    h1=triangle.edges[1].orthogonal_trough(E)
    h2=triangle.edges[2].orthogonal_trough(F)
    rh1=RightAngle(h1,triangle.edges[1],0.2,0,1)
    rh2=RightAngle(h2,triangle.edges[2],0.2,0,1)

    P=Intersection(h1,h2)[0]
    P.put_mark(0.2,0,"\( P\)",automatic_place=(pspict,"W"))


    pspict.DrawGraphs(triangle,h1,h2,rh1,rh2,P)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
