# -*- coding: utf8 -*-
from phystricks import *

mx=-2
Mx=3

def affine(A,B):
    seg=Segment(A,B)
    f=seg.phyFunction().graph(mx,Mx)
    return f

def KKEdcAR():
    pspict,fig = SinglePicture("KKEdcAR")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.6)

    f=affine(Point(1,2),B=Point(4,4))
    g=affine(Point(0,3),B=Point(2,1))

    f.put_mark(0.2,0,"\( d_1\)",pspict=pspict)
    g.put_mark(0.2,45,"\( d_2\)",pspict=pspict,position="corner")

    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
