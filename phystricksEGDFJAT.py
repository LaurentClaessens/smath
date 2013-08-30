# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def EGDFJAT():
    pspict,fig = SinglePicture("EGDFJAT")
    pspict.dilatation(1)

    l=10
    h=5
    rayon=1

    x=var('x')
    I=Point(0,h)
    J=Point(0,0)
    K=Point(l,0)
    L=Point(l,h)

    terrain=Polygon(I,J,K,L)
    M1=Segment(L,I).center()
    M2=Segment(K,J).center()

    mediane=Segment(M1,M2)
    cercle=Circle(mediane.center(),rayon)
    centre=Point(l/2,h/2)

    A=cercle.get_point(90)
    A.put_mark(0.2,45,"\( A\)",automatic_place=pspict)

    B=Point(l/2+l/10,h/10)
    B.put_mark(0.2,90,"\( B\)",automatic_place=pspict)


    pspict.DrawGraphs(terrain,mediane,cercle,A,B,centre)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
