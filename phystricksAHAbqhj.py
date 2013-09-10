# -*- coding: utf8 -*-
from phystricks import *
def AHAbqhj():
    pspict,fig = SinglePicture("AHAbqhj")
    pspict.dilatation(1)

    x=var('x')
    f=LagrangePolynomial([Point(-3,-4),Point(-1,-0.5),Point(0,-1),Point(2,1)]).graph(-3,2.5)
    f.put_mark(0.2,0,"\( f\)",automatic_place=(pspict,"W"))

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
