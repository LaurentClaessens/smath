# -*- coding: utf8 -*-
from phystricks import *
def SLULooXaUibV():
    pspict,fig = SinglePicture("SLULooXaUibV")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(3,0)
    C=Point(0.5,1)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)

    cot=triangle.edges[0]
    cot.divide_in_two(n=2,d=0.1,l=0.2,angle=45,pspict=pspict)
    K=cot.midpoint()
    K.put_mark(0.2,-45,"\( K\)",automatic_place=(pspict,"corner"))

    med=Segment(K,triangle.vertices[2])

    pspict.DrawGraphs(med,K,triangle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
