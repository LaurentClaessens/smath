# -*- coding: utf8 -*-
from phystricks import *
def ILauamX():
    pspict,fig = SinglePicture("ILauamX")
    pspict.dilatation_X(3)
    pspict.dilatation_Y(1)

    x=var('x')
    f=phyFunction(4*x-2).graph(-1,2)

    A=f.get_point(0)
    B=f.get_point(2)

    A.put_mark(0.2,None,"\( A\)",pspict=pspict)
    B.put_mark(0.2,None,"\( B\)",pspict=pspict)

    pspict.DrawGraphs(f,A,B)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

