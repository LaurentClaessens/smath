# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def VUUBooRqdACk():
    pspict,fig = SinglePicture("VUUBooRqdACk")
    pspict.dilatation(0.7)

    l=4
    h=2
    A=Point(0,0)
    B=A+(l,0)
    C=B+(0,-h)
    D=A+(0,-h)
    E=(A+D)*0.5+(-1,0)

    O=C+(1,-0.5)
    O.put_mark(0.15,45,"\( O\)",automatic_place=(pspict,""))

    poly=Polygon(A,B,C,D,E)
    poly.put_mark(0.3,pspict=pspict)

    syms=[  x.symmetric_by(O) for x in poly.vertices ]
    for P in syms :
        pspict.math_BB.append(P,pspict)

    pspict.DrawGraphs(poly,O)
    pspict.grid.main_horizontal.parameters.style="dotted"
    pspict.grid.main_vertical.parameters.style="dotted"
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
