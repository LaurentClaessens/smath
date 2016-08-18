# -*- coding: utf8 -*-
from phystricks import *
def GrapheVarREGMqx():
    pspict,fig = SinglePicture("GrapheVarREGMqx")
    pspict.dilatation(1)

    x=var('x')
    f=HermiteInterpolation([  (-2,2,0),(0,-0.5,0),(2,1,2)  ]).graph(-3,2)
    f.put_mark(0.2,0,"\( f\)",pspict=pspict)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
