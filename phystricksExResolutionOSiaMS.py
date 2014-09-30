# -*- coding: utf8 -*-

from phystricks import *
def ExResolutionOSiaMS():
    pspict,fig = SinglePicture("ExResolutionOSiaMS")
    pspict.dilatation(0.7)

    x=var('x')
    #Plist= [Point(-6,6),Point(-5,3.5),Point(-4,1.5),Point(-3.5,1),Point(-2.5,2),Point(-1.3,1.3),Point(0,0.7),Point(1,0.5),Point(2.3,1.5),Point(3.5,5)] 
    #f=InterpolationCurve(Plist)

    Plist= [Point(-6,6),Point(-3.5,1),Point(-2.5,2),Point(-1.3,1.3),Point(0,0.7),Point(1,0.5),Point(2.3,1.5),Point(3.5,5)] 
    f=LagrangePolynomial(Plist).graph(-4.5,3.5)

    gPlist= [Point(-6,-3),Point(-4,1.5),Point(-3.5,2),Point(-2,0.7),Point(-1.3,1.3),Point(0,2.9),Point(1,3.2),Point(2.3,1.5),Point(3,-1),Point(3.2,-2)] 

    g=LagrangePolynomial(gPlist).graph(-4.5,3.5)
    f.parameters.color="blue"
    g.parameters.color="brown"
    f.put_mark(0.2,0,"\( f\)",automatic_place=pspict)
    g.put_mark(0.2,0,"\( g\)",automatic_place=pspict)


    pspict.DrawGraphs(g,f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
