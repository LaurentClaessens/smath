# -*- coding: utf8 -*-
from phystricks import *
def ITlywMb():
    pspict,fig = SinglePicture("ITlywMb")
    pspict.dilatation(1)

    x=var('x')
    f=HermiteInterpolation( [(-3,6,-1),(-1,2,0),(0,2.5,0.7),(4,0,-1)] ).graph(-3,4.5)  

    pspict.DrawGraphs(f)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
