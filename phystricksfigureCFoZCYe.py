# -*- coding: utf8 -*-
from phystricks import *
def figureCFoZCYe():
    pspict,fig = SinglePicture("figureCFoZCYe")
    pspict.dilatation_Y(0.5)

    x=var('x')
    f=phyFunction(2*x+1).graph(-3,3)
    g=phyFunction(2*x-2).graph(-3,3)
    h=phyFunction(3*x-1).graph(-2,3)

    f.parameters.color="blue"
    g.parameters.color="red"
    h.parameters.color="brown"

    f.put_mark(0.2,0,"\( f\)",pspict=pspict)
    g.put_mark(0.2,0,"\( g\)",pspict=pspict)
    h.put_mark(0.2,0,"\( h\)",pspict=pspict)

    pspict.DrawGraphs(f,g,h)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
