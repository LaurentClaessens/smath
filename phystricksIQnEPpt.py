# -*- coding: utf8 -*-
from phystricks import *
def IQnEPpt():
    pspict,fig = SinglePicture("IQnEPpt")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(2*x+1).graph(-1,2)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.conclude()
    fig.write_the_file()
