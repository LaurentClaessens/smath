# -*- coding: utf8 -*-

from phystricks import *
def ExResolutionOSiaMS():
    pspict,fig = SinglePicture("ExResolutionOSiaMS")
    pspict.dilatation(0.7)

    x=var('x')
    f=InterpolationCurve( [Point(-6,6),Point(-4,1.5),Point(-3.5,1),Point(-2.5,2),Point(-1.3,1.3),Point(0,0.7),Point(1,0.5),Point(2.3,1.5),Point(3.5,5)] )
    g=InterpolationCurve( [Point(-6,-3),Point(-4,1.5),Point(-3.5,2),Point(-2,0.7),Point(-1.3,1.3),Point(0,2.9),Point(1,3.2),Point(2.3,1.5),Point(2.3,1.5),Point(3,-1),Point(3.2,-2)] )
    f.parameters.color="blue"
    g.parameters.color="red"
    f.put_mark(0.2,0,"\( f\)",automatic_place=pspict)
    g.put_mark(0.2,0,"\( g\)",automatic_place=pspict)

    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
