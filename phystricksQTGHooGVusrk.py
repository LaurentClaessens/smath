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

    P.put_mark(0.2,-90,"\( 0.5\)",pspict=pspict,position="N")
    O.put_mark(0.2,-90,"\( O\)",pspict=pspict,position="N")
    A.put_mark(0.2,-90,"\( A\)",pspict=pspict,position="N")
    B.put_mark(0.2,-90,"\( B\)",pspict=pspict,position="N")
    C.put_mark(0.2,-90,"\( C\)",pspict=pspict,position="N")
    D.put_mark(0.2,-90,"\( D\)",pspict=pspict,position="N")

    for p in [P,O,A,B,C,D]:
        p.parameters.symbol=""

    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    axe.Dx=0.1
    axe.no_numbering()

    pspict.DrawGraphs(axe,O,A,B,C,D,P)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

