# -*- coding: utf8 -*-
from phystricks import *
def WPrirwB():
    pspict,fig = SinglePicture("WPrirwB")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(1,2)
    B=Point(3,3)
    C=Point(2,5)
    D=Point(0,4)
    Ap=Point(4,0)

    carre=Polygon(A,B,C,D)

    A.put_mark(0.2,text="\( A\)",pspict=pspict,position="N")
    B.put_mark(0.2,text="\( B\)",pspict=pspict,position="W")
    C.put_mark(0.2,text="\( C\)",pspict=pspict,position="S")
    D.put_mark(0.2,text="\( D\)",pspict=pspict,position="E")
    Ap.put_mark(0.2,text="\( A'\)",pspict=pspict,position="N")
    

    pspict.DrawGraphs(A,B,C,D,Ap,carre)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
