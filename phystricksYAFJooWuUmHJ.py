# -*- coding: utf8 -*-
from phystricks import *
def YAFJooWuUmHJ():
    pspict,fig = SinglePicture("YAFJooWuUmHJ")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(0,1)
    B=Point(5,1)
    C=Point(1,4)

    triangle=Polygon(A,B,C)
    M=Segment(A,B).midpoint()

    mediane=Segment(C,M).dilatation(1.3)

    A.put_mark(0.2,-90-45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,-45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,10,"\( C\)",automatic_place=(pspict,"corner"))
    M.put_mark(0.2,180+45,"\( M\)",automatic_place=(pspict,"corner"))

    AM=Segment(A,M)
    MB=Segment(M,B)

    AM.put_code(n=2,l=0.4,d=0.1,pspict=pspict)
    MB.put_code(n=2,l=0.4,d=0.1,pspict=pspict)

    pspict.DrawGraphs(triangle,A,B,C,mediane,M,AM,MB)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
