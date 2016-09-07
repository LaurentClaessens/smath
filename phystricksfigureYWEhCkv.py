# -*- coding: utf8 -*-
from phystricks import *
def figureYWEhCkv():
    pspict,fig = SinglePicture("figureYWEhCkv")
    pspict.dilatation(0.8)
    #fig.specific_needs="""\makeatletter\@ifundefined{vect}{\\newcommand{\\vect}[1]{\overrightarrow{#1}}}{}\makeatother"""

    A=Point(1,1)
    B=Point(3,-2)
    C=Point(-4,2)

    u=AffineVector(Point(-2,-2),Point(-4,-2))
    v=AffineVector(Point(-3,2),Point(-1,-1))
    w=AffineVector(Point(0,0),Point(-1,2))

    u.parameters.color="blue"
    v.parameters.color="blue"
    w.parameters.color="blue"

    u.put_mark(0.2,None,"\( \\vect{ u }\)",pspict=pspict)
    v.put_mark(0.2,-45,"\( \\vect{ v }\)",pspict=pspict)
    w.put_mark(0.2,None,"\( \\vect{ w }\)",pspict=pspict)

    A.put_mark(0.2,45,"\( A\)",pspict=pspict)
    B.put_mark(0.2,45,"\( B\)",pspict=pspict)
    C.put_mark(0.2,45,"\( C\)",pspict=pspict)

    pspict.DrawGraphs(A,B,C,u,v,w)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
