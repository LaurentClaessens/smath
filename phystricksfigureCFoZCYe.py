# -*- coding: utf8 -*-
from phystricks import *
def figureCFoZCYe():
    pspict,fig = SinglePicture("figureCFoZCYe")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(2*x+1).graph(-3,3)
    g=phyFunction(2*x-2).graph(-3,3)
    h=phyFunction(3*x-1).graph(-3,3)

    f.put_mark(0.2,0,"\( f\)",automatic_place=pspict)
    g.put_mark(0.2,0,"\( g\)",automatic_place=pspict)
    h.put_mark(0.2,0,"\( h\)",automatic_place=pspict)

    pspict.DrawGraphs(f,g,h)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
