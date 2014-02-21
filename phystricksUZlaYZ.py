# -*- coding: utf8 -*-
from phystricks import *

# Cette figure est placée dans un tabular d'un calcul mental. l'input du png est codé en dur.
def UZlaYZ():
    pspict,fig = SinglePicture("UZlaYZ")
    pspict.dilatation_X(3)
    pspict.dilatation_Y(3)

    A=Point(3,1)
    B=Point(1,3)
    v=AffineVector(A,B)

    A.put_mark(0.2,45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,45,"\( B\)",automatic_place=(pspict,"corner"))
    A.parameters.symbol="none"
    B.parameters.symbol="none"

    pspict.DrawGraphs(A,B,v)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

