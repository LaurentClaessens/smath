# -*- coding: utf8 -*-
from phystricks import *
def OWGRRSC():
    pspict,fig = SinglePicture("OWGRRSC")
    pspict.dilatation_Y(0.3)

    x=var('x')
    f=phyFunction(3*x+2).graph(-2,3.5)
    P=f.get_point(1)
    Q=f.get_point(3)

    pspict.DrawGraphs(f,P,Q)
    pspict.axes.single_axeY.Dx=2
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
