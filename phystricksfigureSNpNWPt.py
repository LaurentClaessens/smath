# -*- coding: utf8 -*-
from phystricks import *
def figureSNpNWPt():
    pspict,fig = SinglePicture("figureSNpNWPt")
    pspict.dilatation_X(1)

    moustache=Moustache(0.5,4,5,7,15,h=0.5,delta_y=0.75)

    pspict.DrawGraphs(moustache)
    pspict.DrawDefaultAxes()
    pspict.axes.draw_single_axeY=False
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
