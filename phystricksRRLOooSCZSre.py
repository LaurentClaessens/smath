# -*- coding: utf8 -*-
from phystricks import *
def RRLOooSCZSre():
    pspict,fig = SinglePicture("RRLOooSCZSre")


    pspict.dilatation(0.7)

    A=Point(0,0)
    B=Point(3,0)
    C=Point(-2,2)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)

    pspict.DrawGraphs(triangle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
