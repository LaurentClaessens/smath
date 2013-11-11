# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def UKBImJl():
    pspict,fig = SinglePicture("UKBImJl")
    pspict.dilatation_X(15/4500)
    pspict.dilatation_Y(1.5)

    pspict.Mx_acceptable_BB=5000
    pspict.mx_acceptable_BB=-900

    moustache=Moustache(minimum=900,Q1=1300,M=1500,Q3=1700,maximum=4500,h=0.5,delta_y=1)

    P=Point(1543,1)

    pspict.DrawGraphs(moustache,P)
    pspict.axes.single_axeX.Dx=500
    pspict.axes.single_axeY.no_graduation()
    pspict.grid.Dx=200
    pspict.axes.draw_single_axeY=False
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

