# -*- coding: utf8 -*-
from phystricks import *
def TOIooUindpy():
    pspict,fig = SinglePicture("TOIooUindpy")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=4
    x=1

    carre=Rectangle(  Point(0,l),Point(l,0)  )
    A=carre.NW
    B=carre.NE
    C=carre.SE
    D=carre.SW
       
    A.put_mark(0.2,90+45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,-45,"\( C\)",automatic_place=(pspict,"corner"))
    D.put_mark(0.2,180+45,"\( D\)",automatic_place=(pspict,"corner"))

    N=A+(x,0)
    M=A+(0,-x)

    N.put_mark(0.2,90,"\( N\)",automatic_place=(pspict,"S"))
    M.put_mark(0.2,180,"\( M\)",automatic_place=(pspict,"E"))

    polygon=Polygon(A,N,C,M)
    polygon.parameters.filled()
    polygon.parameters.fill.color="lightgray"

    pspict.DrawGraphs(carre,polygon,A,B,C,D,N,M)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
