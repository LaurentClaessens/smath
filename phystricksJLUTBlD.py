# -*- coding: utf8 -*-
from phystricks import *
def JLUTBlD():
    pspict,fig = SinglePicture("JLUTBlD")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(0.8)

    x=var("x")
    f=phyFunction(3*x-1).graph(-0.5,2)
    g=phyFunction(-x+3).graph(-2,4)

    P=g.get_point(-2)
    Q=g.get_point(4)
    P.parameters.symbol="none"
    Q.parameters.symbol="none"

    f.parameters.color="red"

    pspict.DrawGraphs(f,P,Q)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

