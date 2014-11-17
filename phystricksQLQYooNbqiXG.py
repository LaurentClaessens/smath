# -*- coding: utf8 -*-
from phystricks import *
def QLQYooNbqiXG():
    pspict,fig = SinglePicture("QLQYooNbqiXG")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    P=Point(1,0)
    F=Point(3,-0.3)
    A=Point(4,2)
    
    triangle=Polygon(P,F,A)
    triangle.put_mark(0.2,[  "\( P\)","\( F\)","\( A\)"  ],pspict=pspict)

    pspict.DrawGraphs(triangle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
