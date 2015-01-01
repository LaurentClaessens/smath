# -*- coding: utf8 -*-
from phystricks import *
def QTGHooGVusrk():
    pspict,fig = SinglePicture("QTGHooGVusrk")
    pspict.dilatation_X(5)
    pspict.dilatation_Y(1)

    mx=-0.8
    Mx=0.8

    P=Point(0.5,0)

    O=Point(0,0)
    A=Point(-0.7,0)
    B=Point(-0.5,0)
    C=Point(0.2,0)
    D=Point(0.6,0)

    P.put_mark(0.2,-90,"\( 0.5\)",automatic_place=(pspict,"N"))
    O.put_mark(0.2,-90,"\( O\)",automatic_place=(pspict,"N"))
    A.put_mark(0.2,-90,"\( A\)",automatic_place=(pspict,"N"))
    B.put_mark(0.2,-90,"\( B\)",automatic_place=(pspict,"N"))
    C.put_mark(0.2,-90,"\( C\)",automatic_place=(pspict,"N"))
    D.put_mark(0.2,-90,"\( D\)",automatic_place=(pspict,"N"))

    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    axe.Dx=0.1
    axe.no_numbering()

    pspict.DrawGraphs(axe,O,A,B,C,D,P)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

