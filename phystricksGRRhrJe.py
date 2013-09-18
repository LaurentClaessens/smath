# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def GRRhrJe():
    pspict,fig = SinglePicture("GRRhrJe")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.2)

    x=var('x')
    f1=phyFunction(3*x/2+3).graph(-3,3)
    f2=phyFunction(3*x).graph(-3,3)
    f3=phyFunction(-2*x-2).graph(-3,3)
    f4=phyFunction(x/2-3).graph(-3,3)

    f1.parameters.color="red"
    f4.parameters.color="red"

    f1.put_mark(0.2,0,"\( d_1\)",automatic_place=(pspict,"W"))
    f2.put_mark(0.2,45,"\( d_2\)",automatic_place=(pspict,"W"))
    f3.put_mark(0.2,0,"\( d_3\)",automatic_place=(pspict,"W"))
    f4.put_mark(0.2,0,"\( d_4\)",automatic_place=(pspict,"W"))

    pspict.DrawGraphs(f1,f2,f3,f4)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
