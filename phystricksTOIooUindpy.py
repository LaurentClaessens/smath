# -*- coding: utf8 -*-
from phystricks import *
def TOIooUindpy():
    pspict,fig = SinglePicture("TOIooUindpy")
    pspict.dilatation_X(0.6)
    pspict.dilatation_Y(0.6)

    l=4
    x=1

    carre=Rectangle(  Point(0,l),Point(l,0)  )
    A=carre.NW
    B=carre.NE
    C=carre.SE
    D=carre.SW
       
    A.put_mark(0.2,90+45,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,-45,"\( C\)",pspict=pspict,position="corner")
    D.put_mark(0.2,180+45,"\( D\)",pspict=pspict,position="corner")

    N=A+(x,0)
    M=A+(0,-x)

    N.put_mark(0.2,text="\( N\)",pspict=pspict,position="S")
    M.put_mark(0.2,text="\( M\)",pspict=pspict,position="E")

    for P in [A,B,C,D,M,N]:
        P.parameters.symbol=""

    polygon=Polygon(A,N,C,M)
    polygon.parameters.filled()
    polygon.parameters.fill.color="lightgray"

    pspict.DrawGraphs(carre,polygon,A,B,C,D,N,M)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
