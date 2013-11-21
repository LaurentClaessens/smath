# -*- coding: utf8 -*-
from phystricks import *
def EDnzyzS():
    pspict,fig = SinglePicture("EDnzyzS")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,0)
    B=Point(5,0)
    C=Point(5,2)
    D=Point(0,3)

    M=Point(2,0)

    A.put_mark(0.2,-90,"\( A\)",automatic_place=(pspict,"N"))
    B.put_mark(0.2,-90,"\( B\)",automatic_place=(pspict,"N"))
    M.put_mark(0.2,-90,"\( M\)",automatic_place=(pspict,"N"))

    D.put_mark(0.2,90,"\( D\)",automatic_place=(pspict,"S"))
    C.put_mark(0.2,90,"\( C\)",automatic_place=(pspict,"S"))

    trapeze=Polygon(A,B,C,D)
    s1=Segment(D,M)
    s2=Segment(M,C)

    pspict.DrawGraphs(trapeze,s1,s2,A,B,C,D)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
