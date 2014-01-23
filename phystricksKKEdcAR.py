# -*- coding: utf8 -*-
from phystricks import *

mx=-4
Mx=4

def affine(A,B):
    seg=Segment(A,B)
    f=seg.phyFunction().graph(mx,Mx)
    return f

def KKEdcAR():
    pspict,fig = SinglePicture("KKEdcAR")
    pspict.dilatation(0.7)

    f=affine(Point(1,2),B=Point(4,4))
    g=affine(Point(0,3),B=Point(2,1))

    f.put_mark(0.2,0,"\( d_1\)",automatic_place=pspict)
    g.put_mark(0.2,0,"\( d_2\)",automatic_place=pspict)

    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
