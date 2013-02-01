# -*- coding: utf8 -*-
from phystricks import *
def YAaXJqQ():
    pspict,fig = SinglePicture("YAaXJqQ")
    pspict.dilatation(0.7)

    epsilon=0.2

    x=var('x')
    F=phyFunction((1/(x+3))+2)
    f1=F.graph(-9,-3-epsilon)
    f2=F.graph(-3+epsilon,5)

    pspict.DrawGraphs(f1,f2)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.conclude()
    fig.write_the_file()
