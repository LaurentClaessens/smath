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

    A.put_mark(0.2,-90,"\( A\)",automatic_place=(pspict,"N"))
    B.put_mark(0.2,0,"\( B\)",automatic_place=(pspict,"W"))
    C.put_mark(0.2,90,"\( C\)",automatic_place=(pspict,"S"))
    D.put_mark(0.2,180,"\( D\)",automatic_place=(pspict,"E"))
    Ap.put_mark(0.2,-90,"\( A'\)",automatic_place=(pspict,"N"))
    

    pspict.DrawGraphs(A,B,C,D,Ap,carre)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
