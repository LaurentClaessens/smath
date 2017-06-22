# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def NIGYQHN():
    pspict,fig = SinglePicture("NIGYQHN")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=4
    h=3

    A=Point(0,0)
    B=A+(l,0)
    C=B+(0,h)
    D=A+(0,h)
    M=Point(l,h/3)

    A.put_mark(0.2,225,"\( A\)",pspict=pspict,position="corner")
    B.put_mark(0.2,-45,"\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,45,"\( C\)",pspict=pspict,position="corner")
    D.put_mark(0.2,135,"\( D\)",pspict=pspict,position="corner")
    M.put_mark(0.2,text="\( M\)",pspict=pspict,position="W")

    rectangle=Polygon(A,B,C,D)
    triangle=Polygon(A,B,M)
    poly=Polygon(A,M,C,D)
    poly.filled()
    poly.fill_parameters.color="lightgray"

    pspict.DrawGraphs(A,B,C,D,rectangle,M,triangle,poly)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
