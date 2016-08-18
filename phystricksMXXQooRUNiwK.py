# -*- coding: utf8 -*-
from phystricks import *
def MXXQooRUNiwK():
    pspict,fig = SinglePicture("MXXQooRUNiwK")
    pspict.dilatation(1)

    l=5
    h=4
    perspective=ObliqueProjection(30,0.5)
    A=perspective.point(0,0,0)
    B=perspective.point(l,0,0)
    C=perspective.point(l,0,l)
    D=perspective.point(0,0,l)
    S=perspective.point(l/2,h,l/2)
    H=perspective.point(l/2,0,l/2)

    for pt in [A,B,C,D]:
        pt=pt.rotation(30)

    AB=Segment(A,B)
    BC=Segment(B,C)
    CS=Segment(C,S)
    AS=Segment(A,S)
    BS=Segment(B,S)

    AD=Segment(A,D)
    AD.parameters.style='dashed'
    DC=Segment(D,C)
    DC.parameters.style='dashed'
    SD=Segment(S,D)
    SD.parameters.style='dashed'

    A.put_mark(0.2,180,"\( A\)",pspict=pspict)
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict)
    C.put_mark(0.2,0,"\( C\)",pspict=pspict)
    D.put_mark(0.2,45,"\( D\)",pspict=pspict)
    S.put_mark(0.2,90,"\( S\)",pspict=pspict)
    H.put_mark(0.2,0,"\( H\)",pspict=pspict)
    
    haut=Segment(S,H)
    dig=Segment(A,H)
    for s in [haut,dig]:
        s.parameters.style="dashed"

    rh=RightAngleAOB(S,H,A,n1=0,n2=1)

    no_symbol(A,B,C,D,S,H)
    
    pspict.DrawGraphs(A,B,C,D,S,BS,AB,BC,CS,AS,AD,DC,SD,haut,dig,H,rh)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

