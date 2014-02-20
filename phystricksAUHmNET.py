# -*- coding: utf8 -*-
from phystricks import *
def AUHmNET():
    pspict,fig = SinglePicture("AUHmNET")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    Mx=9
    My=11

    A=Point(Mx,My)
    B=Point(-Mx,My)
    C=Point(Mx,-My)
    D=Point(-Mx,-My)

    linH=Segment( Point(-Mx,0),Point(Mx,0) )
    linH.parameters.add_option("linewidth","1mm")
    linV=Segment( Point(0,My),Point(0,-My) )
    linV.parameters.add_option("linewidth","1mm")

    pspict.DrawGraphs(A,B,C,D,linH,linV)

    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
