# -*- coding: utf8 -*-
from phystricks import *
def XVMLooOHswig():
    pspict,fig = SinglePicture("XVMLooOHswig")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(4,0)
    C=B+(2,1)
    D=A+C-B

    parall=Polygon(A,B,C,D)

    pspict.grid.main_horizontal.parameters.style="dotted"
    pspict.grid.main_vertical.parameters.style="dotted"

    pspict.DrawGraphs(parall)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
