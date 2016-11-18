# -*- coding: utf8 -*-
from phystricks import *
def OLuvnaY():
    pspict,fig = SinglePicture("OLuvnaY")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    c=5
    A=Point(0,0)
    B=A+(c,0)
    C=B+(0,c)
    D=C+(-c,0)

    gd_carre=Polygon(A,B,C,D)
    l=2
    N=D+(l,0)
    M=B+(0,l)
    P=Point(N.x,M.y)

    pt_carre=Polygon(N,P,M,C)
    gris=Polygon(N,P,M,A)
    gris.parameters.filled()
    gris.parameters.fill.color="lightgray"

    A.put_mark(0.2,180+45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,45,"\( C\)",pspict=pspict,position="corner")
    D.put_mark(0.2,90+45,"\( D\)",pspict=pspict,position="corner")
    N.put_mark(0.2,text="\( N\)",pspict=pspict,position="S")
    P.put_mark(0.2,45,"\( P\)",pspict=pspict,position="corner")
    M.put_mark(0.2,text="\( M\)",pspict=pspict,position="W")


    pspict.DrawGraphs(gd_carre,pt_carre,gris,A,B,C,D,N,P,M)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
