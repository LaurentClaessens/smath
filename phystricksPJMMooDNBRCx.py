# -*- coding: utf8 -*-
from phystricks import *
def PJMMooDNBRCx():
    pspict,fig = SinglePicture("PJMMooDNBRCx")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(1)

    Mx=4.7
    mx=-5

    O=Point(0,0)
    A=Point(-4,0)
    B=Point(2,0)
    C=Point(4.5,0)
    D=Point(-2.5,0)

    O.put_mark(0.2,text="\( O\)",pspict=pspict,position="N")
    A.put_mark(0.2,text="\( A\)",pspict=pspict,position="N")
    B.put_mark(0.2,text="\( B\)",pspict=pspict,position="N")
    C.put_mark(0.2,text="\( C\)",pspict=pspict,position="N")
    D.put_mark(0.2,text="\( D\)",pspict=pspict,position="N")

    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    axe.no_numbering()

    pspict.DrawGraphs(axe,O,A,B,C,D)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
