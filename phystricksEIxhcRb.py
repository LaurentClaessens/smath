# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def EIxhcRb():
    pspict,fig = SinglePicture("EIxhcRb")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)
    x=var('x')

    A=Point(-3,1)
    B=Point(-1,0)
    D=Point(2,0)
    E=Point(3,0)
    F=Point(7,0)
    k=Segment(Point(-3,1),Point(-1,0))
    C=k.get_point(1)

    s1=Segment(A,C)
    s2=Segment(C,D)
    f=LagrangePolynomial( [D,E,F,Point(2.5,-1),Point(5,2)] ).graph(2,7)
    f=phyFunction(  5*(x-2)*(x-3) ).graph(2,3)
    g=phyFunction(  -(x-3)*(x-7)/3 ).graph(3,7)

    f.parameters.color="black"
    g.parameters.color="black"

    pspict.DrawGraphs(s1,s2,f,g)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

