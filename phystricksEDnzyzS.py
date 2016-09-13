# -*- coding: utf8 -*-
from phystricks import *
def EDnzyzS():
    pspict,fig = SinglePicture("EDnzyzS")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    A=Point(0,0)
    B=Point(5,0)
    C=Point(5,2)
    D=Point(0,3)

    M=Point(2,0)

    A.put_mark(0.2,text="\( A\)",pspict=pspict,position="N")
    B.put_mark(0.2,text="\( B\)",pspict=pspict,position="N")
    M.put_mark(0.2,text="\( M\)",pspict=pspict,position="N")

    D.put_mark(0.2,text="\( D\)",pspict=pspict,position="S")
    C.put_mark(0.2,text="\( C\)",pspict=pspict,position="S")

    trapeze=Polygon(A,B,C,D)
    s1=Segment(D,M)
    s2=Segment(M,C)

    pspict.DrawGraphs(trapeze,s1,s2,A,B,C,D,M)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
