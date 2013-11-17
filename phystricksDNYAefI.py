# -*- coding: utf8 -*-
from phystricks import *
def DNYAefI():
    pspict,fig = SinglePicture("DNYAefI")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    minimum=1
    Maximum=10
    Q1=2
    mediane=4
    Q3=5
    moustache=Moustache(minimum,Q1,mediane,Q3,Maximum,h=0.5,delta_y=0.75)

    pspict.DrawGraphs(moustache)
    pspict.axes.draw_single_axeY=False
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
