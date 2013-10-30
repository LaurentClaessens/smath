# -*- coding: utf8 -*-
from phystricks import *
def KDtwIJf():
    pspict,fig = SinglePicture("KDtwIJf")
    pspict.dilatation_X(0.15)
    pspict.dilatation_Y(1)

    pspict.Mx_acceptable_BB=105

    minimum=0
    Maximum=100
    Q1=26
    mediane=50
    Q3=76
    moustache=Moustache(minimum,Q1,mediane,Q3,Maximum,h=0.5,delta_y=0.75)



    pspict.DrawGraphs(moustache)

    #pspict.DrawDefaultAxes()
    #pspict.axes.draw_single_axeY=False
    #pspict.axes.single_axeX.Dx=5
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
