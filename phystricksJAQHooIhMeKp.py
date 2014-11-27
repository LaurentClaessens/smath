# -*- coding: utf8 -*-
from phystricks import *
def JAQHooIhMeKp():
    pspict,fig = SinglePicture("JAQHooIhMeKp")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    L=Point(0,0)
    K=Point(6,0)
    M=Point(2,4)

    triangle=Polygon(L,K,M)
    triangle.put_mark(0.2,['\( L\)',"\( K\)","\( M\)"],pspict=pspict)

    hauteur=Segment(K,M).orthogonal_trough(L).dilatation(1.5)
    hauteur.parameters.color='blue'
    rh=RightAngle( Segment(K,M),hauteur,0.2,0,0 )

    mediane=Segment(K,Segment(L,M).midpoint()).dilatation(1.5)
    mediane.parameters.color="red"
    triangle.edges[2].divide_in_two(2,d=0.1,l=0.3,pspict=pspict)

    pspict.DrawGraphs(hauteur,rh,mediane,triangle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
