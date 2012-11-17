# -*- coding: utf8 -*-
from phystricks import *
def figureYWEhCkv():
    pspict,fig = SinglePicture("figureYWEhCkv")
    pspict.dilatation(0.8)
    fig.specific_needs="""\makeatletter\@ifundefined{vect}{\\newcommand{\\vect}[1]{\overrightarrow{#1}}}{}\makeatother"""

    A=Point(1,1)
    B=Point(-2,3)
    C=Point(2,-4)

    u=AffineVector(Point(3,1),Point(3,-1))
    v=AffineVector(Point(-2,-3),Point(-1,-1))
    w=AffineVector(Point(0,0),Point(2,-1))

    u.parameters.color="red"
    v.parameters.color="blue"
    w.parameters.color="green"

    u.put_mark(0.2,u.advised_mark_angle,"\( \\vect{ u }\)",automatic_place=pspict)
    v.put_mark(0.2,-45,"\( \\vect{ v }\)",automatic_place=pspict)
    w.put_mark(0.2,w.advised_mark_angle+180,"\( \\vect{ w }\)",automatic_place=pspict)

    A.put_mark(0.2,45,"\( A\)",automatic_place=pspict)
    B.put_mark(0.2,45,"\( B\)",automatic_place=pspict)
    C.put_mark(0.2,45,"\( C\)",automatic_place=pspict)

    pspict.DrawGraphs(A,B,C,u,v,w)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
