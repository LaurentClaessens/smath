# -*- coding: utf8 -*-
from phystricks import *
def GOARooHSKUuw():
    pspict,fig = SinglePicture("GOARooHSKUuw")
    pspict.dilatation(2)
    pspict.rotation(0)

    A=Point(0,0)
    B=Point(4,0)
    C=Point(5,4)

    trigA=Polygon(A,B,C)

    D=trigA.edges[2].midpoint()
    E=Segment(D,B).midpoint()
    DB=Segment(D,B)
    AE=Segment(A,E)
    F=AE.midpoint()

    trigD=Polygon(D,E,F)
    trigD.put_mark(0.3,points_names="DEF",pspict=pspict)

    trigA.put_mark(0.3,pspict=pspict)
    trigA.edges[2].divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspict)
    DB.divide_in_two(n=1,d=0.1,l=0.3,angle=45,pspict=pspict)
    AE.divide_in_two(n=3,d=0.1,l=0.3,angle=45,pspict=pspict)

    no_symbol(trigA.vertices,trigD.vertices)
    pspict.DrawGraphs(trigA,trigD,DB,AE)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
