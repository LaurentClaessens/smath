# -*- coding: utf8 -*-
from phystricks import *
def LVALooSubNDJ():
    pspict,fig = SinglePicture("LVALooSubNDJ")
    pspict.dilatation(1)
    pspict.rotation(45)

    l=3
    L=4
    h=5
    perspective=ObliqueProjection(30,0.8)
    A=perspective.point(0,0,0)
    B=perspective.point(L,0,0)
    C=perspective.point(L,0,l)
    D=perspective.point(0,0,l)
    S=perspective.point(L/2,-h,l/2)

    AB=Segment(A,B)
    BC=Segment(B,C)
    CS=Segment(C,S)
    AS=Segment(A,S)
    BS=Segment(B,S)

    AD=Segment(A,D)
    AD.put_mark(0.2,angle=None,added_angle=0,text="\SI{5}{\centi\meter}",pspict=pspict)
    DC=Segment(D,C)
    DC.put_mark(0.3,angle=None,added_angle=0,text="\SI{2}{\centi\meter}",pspict=pspict)
    SD=Segment(S,D)
    SD.parameters.style='dashed'
    #DC.parameters.style='dashed'
    #AD.parameters.style='dashed'

    A.put_mark(0.2,180,"\( A\)",pspict=pspict)
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict)
    C.put_mark(0.2,0,"\( C\)",pspict=pspict)
    D.put_mark(0.2,90+45,"\( D\)",pspict=pspict)
    S.put_mark(0.2,-90,"\( S\)",pspict=pspict)

    no_symbol(A,B,C,D,S)
    
    pspict.DrawGraphs(A,B,C,D,S,BS,AB,BC,CS,AS,AD,DC,SD)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

