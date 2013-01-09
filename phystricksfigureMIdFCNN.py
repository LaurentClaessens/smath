# -*- coding: utf8 -*-
from phystricks import *
def figureMIdFCNN():
    pspict,fig = SinglePicture("figureMIdFCNN")
    pspict.dilatation(1)

    a=4
    epsilon=0.2

    x=var('x')
    F=phyFunction(1/x)
    f=F.graph(-a,-epsilon)
    g=F.graph(epsilon,a)

    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
