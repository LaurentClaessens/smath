# -*- coding: utf8 -*-
from phystricks import *
def AUHmNET():
    pspict,fig = SinglePicture("AUHmNET")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    A=Point(9,11)
    B=Point(-9,11)
    C=Point(9,-11)
    D=Point(-9,-11)

    pspict.DrawGraphs(A,B,C,D)

    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
