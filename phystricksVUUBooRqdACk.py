# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def VUUBooRqdACk():
    pspict,fig = SinglePicture("VUUBooRqdACk")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=4
    h=2
    A=Point(0,0)
    B=A+(l,0)
    C=B+(0,-h)
    D=A+(0,-h)
    E=(A+D)*0.5+(-1,0)

    poly=Polygon(A,B,C,D,E)
    poly.put_mark(0.2,pspict=pspict)

    syms=[  x.symmetric_by(C) for x in poly.vertices ]
    for P in syms :
        #P.parameters.symbol="none"
        pspict.math_BB.append(P,pspict)

    pspict.DrawGraphs(poly)
    pspict.grid.main_horizontal.parameters.style="dotted"
    pspict.grid.main_vertical.parameters.style="dotted"
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
