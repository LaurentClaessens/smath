# -*- coding: utf8 -*-
from phystricks import *
def PUGmLBC():
    pspict,fig = SinglePicture("PUGmLBC")

    pspict.dilatation_X(0.02)
    pspict.dilatation_Y(1)

    pspict.Mx_acceptable_BB=2000
    pspict.mx_acceptable_BB=-2000

    b1=Polygon(  Point(100,0),Point(200,0),Point(200,3),Point(100,3)  )
    b2=Polygon(  Point(500,0),Point(600,0),Point(600,2),Point(500,2)  )

    for k in [b1,b2]:
        k.parameters.hatched()
        k.parameters.hatch.color="red"

    pspict.axes.single_axeX.put_mark(0.2,text="CA",pspict=pspict,position="N")
    pspict.axes.single_axeX.Dx=100

    pspict.DrawGraphs(b1,b2)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
