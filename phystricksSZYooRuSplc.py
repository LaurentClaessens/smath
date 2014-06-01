# -*- coding: utf8 -*-
from phystricks import *
def SZYooRuSplc():
    pspict,fig = SinglePicture("SZYooRuSplc")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    h=8
    l=12
    c=3
    A=Point(0,h)
    B=Point(l,h)
    C=Point(l,0)
    D=Point(0,0)

    M=Point(B.x-c,B.y)
    P=Point(M.x,D.y+c)
    Q=Point(B.x,P.y)
    R=Point(M.x,D.y)
    N=Point(D.x,D.y+c)

    A.put_mark(0.2,90+45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,-45,"\( C\)",automatic_place=(pspict,"corner"))
    D.put_mark(0.2,-90-45,"\( D\)",automatic_place=(pspict,"corner"))

    R.put_mark(0.2,-90,"\( R\)",automatic_place=(pspict,"N"))
    P.put_mark(0.2,45,"\( P\)",automatic_place=(pspict,"corner"))
    Q.put_mark(0.2,0,"\( Q\)",automatic_place=(pspict,"W"))
    M.put_mark(0.2,90,"\( M\)",automatic_place=(pspict,"S"))
    N.put_mark(0.2,180,"\( N\)",automatic_place=(pspict,"E"))

    rectangle=Polygon(A,B,C,D)
    gris1=Polygon(A,M,P,N)
    gris2=Polygon(P,Q,C,R)

    for gr in [gris1,gris2]:
        gr.parameters.filled()
        gr.parameters.fill.color="lightgray"

    pspict.DrawGraphs(rectangle,gris1,gris2,A,B,C,D,M,N,P,Q,R)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
