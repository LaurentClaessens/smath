# -*- coding: utf8 -*-
from phystricks import *
def figureNNgEEzx():
    pspict,fig = SinglePicture("figureNNgEEzx")
    pspict.dilatation(1)

    A=Point(3,2)
    B=Point(1,3)
    O=Point(0,0)
    v=AffineVector(A,B)
    M=Point(0,0)+v
    w=AffineVector(O,M)

    A.put_mark(0.2,0,"\( A\)",pspict=pspict)
    B.put_mark(0.2,90,"\( B\)",pspict=pspict)
    M.put_mark(0.2,135,"\( M\)",pspict=pspict)
    O.put_mark(0.2,45,"\( O\)",pspict=pspict)
    A.parameters.symbol="x"
    B.parameters.symbol="x"
    M.parameters.symbol="x"

    pspict.DrawGraphs(A,B,v,M,w,O)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
