# -*- coding: utf8 -*-
from phystricks import *
def figureYWEhCkv():
    pspict,fig = SinglePicture("figureYWEhCkv")
    pspict.dilatation(0.7)

    A=Point(1,1)
    B=Point(-2,3)
    C=Point(2,-4)

    u=AffineVector(Point(3,1),Point(3,-1))
    v=AffineVector(Point(-2,-3),Point(-1,-1))
    w=AffineVector(Point(0,0),Point(2,-1))

    u.parameters.color="red"
    v.parameters.color="blue"
    w.parameters.color="green"

    A.put_mark(0.2,45,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,45,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,45,"\( C\)",automatic_place=pspict)

    pspict.DrawGraphs(A,B,C,u,v,w)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
