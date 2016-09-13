# -*- coding: utf8 -*-
from phystricks import *
def BIlgjwy():
    pspict,fig = SinglePicture("BIlgjwy")
    pspict.dilatation(0.5)

    h=5

    P=Point(0,0)
    A=Point(4,0)
    B=Point(7,0)
    N=Point( A.x,2 )

    C=Point(B.x+4,0)
    D=Point(C.x,h)
    E=Point(B.x,h)

    M=Intersection( Segment(P,N),Segment(E,B) )[0]

    lumiere=Segment(P,M)
    lumiere.parameters.style="dashed"

    AN=Segment(A,N)
    AN.put_mark(0.1,0,"Muret",pspict=pspict)

    BM=Segment(B,M)
    CD=Segment(C,D)
    BE=Segment(B,E)
    PC=Segment(P,C).dilatation(1.1)

    F=Point(  Segment(E,D).midpoint().x,E.y+2 )
    FE=Segment(F,E).dilatationF(1.3)
    FD=Segment(F,D).dilatationF(1.3)
    pspict.DrawGraphs(BM,CD,PC,BE,FE,FD)

    P.put_mark(0.2,-90,"\( P\)",pspict=pspict)
    A.put_mark(0.2,-90,"\( A\)",pspict=pspict)
    B.put_mark(0.2,-90,"\( B\)",pspict=pspict)
    N.put_mark(0.2,90,"\( N\)",pspict=pspict)
    M.put_mark(0.2,0,"\( M\)",pspict=pspict)

    pspict.DrawGraphs(P,A,B,N,M,lumiere,AN)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
