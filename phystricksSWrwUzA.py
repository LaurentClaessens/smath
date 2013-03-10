# -*- coding: utf8 -*-
from phystricks import *
def SWrwUzA():
    pspict,fig = SinglePicture("SWrwUzA")
    pspict.dilatation(0.3)

    x=var('x')
    f=phyFunction(1/x).graph(-10,10)
    f.cut_y(-10,10)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

