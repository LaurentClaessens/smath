# -*- coding: utf8 -*-
from phystricks import *
def VUOCooYkrktO():
    pspict,fig = SinglePicture("VUOCooYkrktO")
    pspict.dilatation(1)

    A=Point(0,0)
    B=Point(3,2)
    C=Point(4,0)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)

    S=triangle.edges[2].midpoint()
    S.put_mark(0.2,-90,"\( S\)",pspict=pspict,position="N")

    pspict.DrawGraphs(triangle,S)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

