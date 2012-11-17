# -*- coding: utf8 -*-
from phystricks import *
def ExoVectoFRPXxB():
    pspict,fig = SinglePicture("ExoVectoFRPXxB")
    pspict.dilatation(1)

    fig.specific_needs="""\makeatletter\@ifundefined{vect}{\\newcommand{\\vect}[1]{\overrightarrow{#1}}}{}\makeatother"""

    A=Point(0,0)
    U=Point(3,1)
    V=Point(2,-4)
    O=Point(1,-1)

    u=AffineVector(A,U)
    v=AffineVector(A,V)

    u.put_mark(0.2,0,"\(  \\vect{ u }\)",automatic_place=pspict)
    v.put_mark(0.2,0,"\(  \\vect{ v }\)",automatic_place=pspict)

    O.put_mark(0.2,0,"\( O\)",automatic_place=pspict)

    pspict.DrawGraphs(O,u,v)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
