# -*- coding: utf8 -*-
from phystricks import *
def MRBWooRCSkaB():
    pspict,fig = SinglePicture("MRBWooRCSkaB")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    O=Point(0,0)
    r=3

    O.put_mark(0.2,0,"\( O\)",automatic_place=(pspict,"W"))

    cercle=Circle(O,r)
    A=cercle.get_point(45)
    B=cercle.get_point(90)
    C=cercle.get_point(180)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,["\( A\)","\( B\)","\( C\)"],pspict=pspict)


    mid=[  seg.midpoint() for seg in triangle.edges  ]
    mediatrices=[  Segment(O,m).dilatation(1.5) for m in mid ]

    for i,edge in enumerate(triangle.edges) :
        edge.divide_in_two(n=i+1,d=0.1,l=0.3,pspict=pspict)

    for i in [0,1,2]:
        cot=triangle.edges[i]
        med=mediatrices[i]
        rh=RightAngle(med,cot,0,0)
        pspict.DrawGraphs(rh)

    pspict.DrawGraphs(triangle,mediatrices,O)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
