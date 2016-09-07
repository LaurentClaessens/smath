# -*- coding: utf8 -*-
from phystricks import *
def STSooGUprbS():
    pspict,fig = SinglePicture("STSooGUprbS")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(0.5)

    mx=-8
    Mx=3

    x=var('x')
    f=phyFunction((x-1)/(2*x+8)).graph(mx,Mx)

    f.cut_y(-8,8)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
