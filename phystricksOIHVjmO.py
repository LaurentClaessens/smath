# -*- coding: utf8 -*-
from phystricks import *
def OIHVjmO():
    pspict,fig = SinglePicture("OIHVjmO")
    pspict.dilatation_Y(0.2)

    ymin=-10
    ymax=35
    x=var('x')
    f=phyFunction(   (x+1)*(1-x)/(x+3)    ).graph(-10,5)
    f.cut_y(ymin,ymax,plotpoints=3000)

    v=Segment( Point(-3,ymin),Point(-3,ymax)  )
    v.parameters.color="red"

    pspict.DrawGraphs(f,v)
    pspict.axes.single_axeY.Dx=5
    #pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
