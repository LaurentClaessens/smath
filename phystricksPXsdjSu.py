# -*- coding: utf8 -*-
from phystricks import *
def PXsdjSu():
    pspict,fig = SinglePicture("PXsdjSu")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    f=LagrangePolynomial([Point(-1,-0),Point(0,0),Point(3,2),Point(6,-3)]).graph(-1.5,5.3)
    f.put_mark(0.2,0,"\( f\)",automatic_place=(pspict,"W"))

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
