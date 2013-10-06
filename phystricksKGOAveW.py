# -*- coding: utf8 -*-
from phystricks import *
from phystricksLectureGraphnrkEEM import f


def KGOAveW():
    pspict,fig = SinglePicture("KGOAveW")

    pspict.dilatation_X(2.5)
    pspict.dilatation_Y(0.7)

    Z=[z.real_part() for z in f.inverse(0)]

    A=Point(Z[0],0)
    B=Point(Z[1],0)
    C=Point(Z[2],0)

    A.put_mark(0.2,-90,"\( A\)",automatic_place=(pspict,"N"))
    B.put_mark(0.2,-90,"\( B\)",automatic_place=(pspict,"N"))
    C.put_mark(0.2,-90,"\( C\)",automatic_place=(pspict,"N"))

    pspict.axes.single_axeX.Dx=0.5
    pspict.DrawGraphs(f,A,B,C)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
