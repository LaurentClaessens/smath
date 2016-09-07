# -*- coding: utf8 -*-
from phystricks import *
def QGaeERu():
    pspict,fig = SinglePicture("QGaeERu")
    pspict.dilatation_X(0.3)
    pspict.dilatation_Y(0.045)

    pspict.My_acceptable_BB=200

    x=var('x')
    f=phyFunction(-x**2+20*x+21).graph(0,21)

    pspict.DrawGraphs(f)

    pspict.axes.single_axeX.Dx=2
    pspict.axes.single_axeY.Dx=10
    pspict.grid.Dx=pspict.single_axeX.Dx
    pspict.grid.Dy=pspict.single_axeY.Dx
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
