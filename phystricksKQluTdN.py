# -*- coding: utf8 -*-
from phystricks import *
def KQluTdN():
    pspict,fig = SinglePicture("KQluTdN")
    pspict.dilatation_X(2)
    pspict.dilatation_Y(0.5)

    x=var('x')
    f=phyFunction(-x**2+2*x+2).graph(-1.5,3.5)

    a=-1
    b=2

    A=f.get_point(a)
    B=f.get_point(b)

    ta=f.get_tangent_segment(a).graph(-2,0.5)
    tb=f.get_tangent_segment(b).graph(1,4)

    pspict.DrawGraphs(f,A,B,ta,tb)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
