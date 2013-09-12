# -*- coding: utf8 -*-

from phystricks import *
def ExoIntersectionCourbenzIxXd():
    pspict,fig = SinglePicture("ExoIntersectionCourbenzIxXd")
    pspict.dilatation(0.7)

    x=var('x')
    points_list=[ Point(1,0),Point(1.5,2),Point(3,4),Point(4,3),Point(5,2),Point(7,4),Point(8,5) ]
    curve=InterpolationCurve(points_list)
    curve.put_mark(0.2,0,"\( f\)",automatic_place=pspict)

    f=phyFunction(x).graph(-1,8)
    f.put_mark(0.2,0,"\( y=x\)",automatic_place=pspict)

    pspict.DrawGraphs(curve,f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
