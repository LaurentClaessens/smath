# -*- coding: utf8 -*-
from phystricks import *
def XPqLRCF():
    pspict,fig = SinglePicture("XPqLRCF")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(-x+1).graph(-2,4)
    g=phyFunction(2*x-3).graph(-1,3.5)
    h=phyFunction(-3*x+1).graph(-1,1)

    f.put_mark(0.2,0,"\( f\)",automatic_place=(pspict,"W"))
    g.put_mark(0.2,0,"\( g\)",automatic_place=(pspict,"W"))
    h.put_mark(0.2,0,"\( h\)",automatic_place=(pspict,"W"))

    g.parameters.color="brown"
    h.parameters.color="red"

    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
