# -*- coding: utf8 -*-
from phystricks import *

# Cette figure est d'un calcul mental et le png est inclu en dur.
def GUEjmmR():
    pspict,fig = SinglePicture("GUEjmmR")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    c=3
    A=Point(0,0)
    B=Point(c,0)
    C=Point(c,c)
    D=Point(0,c)

    carre=Polygon(A,B,C,D)
    A.put_mark(0.2,180+45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,-45,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,45,"\( C\)",automatic_place=(pspict,"corner"))
    D.put_mark(0.2,90+45,"\( D\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(carre,A,B,C,D)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
