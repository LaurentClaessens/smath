# -*- coding: utf8 -*-
from phystricks import *
def MITEooHPaqZu():
    pspict,fig = SinglePicture("MITEooHPaqZu")

    pspict.dilatation(0.5)

    A=Point(0,0)
    B=Point(5,0)
    C=Point(2,3)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)

    pspict.DrawGraphs(triangle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
