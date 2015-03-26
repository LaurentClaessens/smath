# -*- coding: utf8 -*-

from phystricks import *
def ExoIntersectionCourbenzIxXd():
    pspict,fig = SinglePicture("ExoIntersectionCourbenzIxXd")
    pspict.dilatation(0.7)

    x=var('x')
    points_list=[ Point(1,0),Point(1.5,2),Point(3,4),Point(4,3),Point(5,2),Point(6,3),Point(7,4),Point(8,5) ]

    curve2=InterpolationCurve(points_list,mode=6)
    curve2.parameters.color="cyan"

    #curve=LagrangePolynomial(points_list).graph(1,8)
    #curve.parameters.color="brown"
    #curve.put_mark(0.2,0,"\( f\)",automatic_place=pspict)
    #curve3=InterpolationCurve(points_list,mode=4)
    #curve3.parameters.color="green"

    f=phyFunction(x).graph(-1,8)
    f.put_mark(0.2,0,"\( y=x\)",automatic_place=pspict)

    pspict.DrawGraphs(f,curve2)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
