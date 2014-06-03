# -*- coding: utf8 -*-
from phystricks import *
def JSFooDBSHFo():
    pspict,fig = SinglePicture("JSFooDBSHFo")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    h=7
    l=12
    c=3
    A=Point(0,h)
    B=Point(l,h)
    C=Point(l,0)
    D=Point(0,0)

    M=Point(B.x-c,B.y)
    P=Point(M.x,B.y-c)
    N=Point(B.x,P.y)

    A.put_mark(0.2,90+45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,-45,"\( C\)",automatic_place=(pspict,"corner"))
    D.put_mark(0.2,-90-45,"\( D\)",automatic_place=(pspict,"corner"))

    P.put_mark(0.2,90+45,"\( P\)",automatic_place=(pspict,"corner"))
    M.put_mark(0.2,90,"\( M\)",automatic_place=(pspict,"S"))
    N.put_mark(0.2,0,"\( N\)",automatic_place=(pspict,"W"))

    rectangle=Polygon(A,B,C,D)
    gris1=Polygon(M,B,N,P)
    gris2=Polygon(D,C,N)

    for gr in [gris1,gris2]:
        gr.parameters.filled()
        gr.parameters.fill.color="lightgray"

    pspict.DrawGraphs(rectangle,gris1,gris2,A,B,C,D,P,M,N)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
