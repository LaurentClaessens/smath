# -*- coding: utf8 -*-

import string

from phystricks import *
def GARYooJCnpFS():
    pspict,fig = SinglePicture("GARYooJCnpFS")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(4,1)
    C=Point(3,3)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)
    
    for i in [0,1,2]:
        P=triangle.vertices[i]
        cot=triangle.edges[ (i+1)%3 ]
        M=cot.midpoint()
        med=Segment(M,P).dilatation(1.5)
        cot.divide_in_two(n=i+1,d=0.1,l=0.3,pspict=pspict)
        pspict.DrawGraph(med)

    pspict.DrawGraphs(triangle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
