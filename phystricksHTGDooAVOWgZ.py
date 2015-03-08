# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def HTGDooAVOWgZ():
    pspict,fig = SinglePicture("HTGDooAVOWgZ")

    pspict.dilatation(0.48)

    l=3
    L=4
    h=5
    perspective=ObliqueProjection(30,0.5)
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
    DC=Segment(D,C)
    SD=Segment(S,D)
    SD.parameters.style='dashed'
    #DC.parameters.style='dashed'
    #AD.parameters.style='dashed'

    A.put_mark(0.2,180,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,-45,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,0,"\( C\)",automatic_place=pspict)
    D.put_mark(0.2,90+45,"\( D\)",automatic_place=pspict)
    S.put_mark(0.2,-90,"\( S\)",automatic_place=pspict)

    no_symbol(A,B,C,D,S)
    
    pspict.DrawGraphs(A,B,C,D,S,BS,AB,BC,CS,AS,AD,DC,SD)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

