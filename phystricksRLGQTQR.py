# -*- coding: utf8 -*-
from phystricks import *
def RLGQTQR():
    pspict,fig = SinglePicture("RLGQTQR")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(0.5)

    x=var('x')
    f=phyFunction(2*x-4).graph(-1.3,4)
    A=Point(0,-4)
    B=Point(3,2)

    A.put_mark(0.2,-45,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,-45,"\( B\)",automatic_place=pspict)

    pspict.DrawGraphs(f,A,B)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
