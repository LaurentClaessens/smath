# -*- coding: utf8 -*-
from phystricks import *
def WRXbDCo():
    pspict,fig = SinglePicture("WRXbDCo")
    pspict.dilatation_X(3)
    pspict.dilatation_Y(0.2)

    x=var('x')
    f=LagrangePolynomial( [Point(0,15),Point(1,20),Point(3,0)] ).graph(0,3)

    #f.parameters.color="green"

    pspict.DrawGraphs(f)
    pspict.axes.single_axeY.Dx=5
    pspict.grid.Dx=1
    pspict.grid.Dy=5
    pspict.grid.num_subX=0
    pspict.grid.num_subY=1

    pspict.axes.do_mx_enlarge=False
    pspict.axes.do_my_enlarge=False

    pspict.DrawDefaultAxes()
    # TODO : si on enlève la grille, alors le do_mx_enlarge est pris en compte.
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
