# -*- coding: utf8 -*-
from phystricks import *
def RRlBSZg():
    pspict,fig = SinglePicture("RRlBSZg")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(0.8)

    x=var("x")
    f=phyFunction(-x+1).graph(-3,2.5)
    g=phyFunction(-2*x+3).graph(-3,2.5)

    #P=g.get_point(-2)
    #Q=g.get_point(4)
    #P.parameters.symbol="none"
    #Q.parameters.symbol="none"

    f.parameters.color="red"

    #pspict.DrawGraphs(f,P,Q)
    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
