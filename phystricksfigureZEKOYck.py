# -*- coding: utf8 -*-
from phystricks import *
def figureZEKOYck():
    pspict,fig = SinglePicture("figureZEKOYck")
    pspict.dilatation(1)

    x=var('x')
    f=LagrangePolynomial( Point(-2,-1),Point(-4,1),Point(0,1) ).graph(-5,1.5)
    g=phyFunction(f(x-1)).graph(-5,2)
    h=phyFunction(-f(x-4)+1).graph(-1,5)

    f.parameters.color="blue"
    g.parameters.color="red"
    h.parameters.color="green"

    pspict.DrawGraphs(f,g,h)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

