# -*- coding: utf8 -*-
from phystricks import *

l=2
h=2

def petit(x,y):
    return Polygon(  Point(l*x,h*y),Point(l*(x+1),h*y),Point(l*(x+1),h*(y+1)),Point(l*x,h*(y+1))  )

def UKRHooEvocBg():
    pspict,fig = SinglePicture("UKRHooEvocBg")
    pspict.dilatation(0.5)

    for x in range(0,4):
        a=petit(x,0)
        b=petit(x,1)
        a.filled()
        a.fill_parameters.color='lightgray'
        b.filled()
        b.fill_parameters.color='lightgray'
        pspict.DrawGraphs(a,b)

    for x in range(0,4):
        b=petit(x,2)
        pspict.DrawGraphs(b)

    for x in range(0,3):
        b=petit(x,2)
        b.hatched()
        b.hatch_parameters.color='lightgray'
        pspict.DrawGraphs(b)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
