# -*- coding: utf8 -*-
from phystricks import *
def AMXQooFiUqRS():
    pspict,fig = SinglePicture("AMXQooFiUqRS")
    pspict.dilatation(0.6)

    A=Point(0,0)
    B=Point(0,4)
    C=Point(1,2)
    D=Point(1,1)

    trap=Polygon(A,B,C,D)
    trap.put_mark(0.2,pspict=pspict)

    trap.hatched()
    trap.hatch_parameters.color="lightgray"

    no_symbol(trap.vertices)
    pspict.DrawGraphs(trap)

    pspict.grid.main_horizontal.parameters.style="dotted"
    pspict.grid.main_vertical.parameters.style="dotted"


    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

