# -*- coding: utf8 -*-
from phystricks import *
def JXWXdJI():
    pspict,fig = SinglePicture("JXWXdJI")
    pspict.dilatation_X(0.03)
    pspict.dilatation_Y(1)

    CA=[100,101,105,502,503]
    # Attention : ces CA sont utilisés explicitement aussi dans phystricksPUGmLBC

    pts=[  Point(x,1) for x in CA ]

    pspict.Mx_acceptable_BB=1000
    pspict.mx_acceptable_BB=-1000

    pspict.axes.single_axeX.put_mark(0.2,-90,"CA",pspict=pspict,position="N")
    pspict.axes.single_axeX.Dx=100
    pspict.axes.single_axeY.put_mark(0.2,180,"Effectifs",pspict=pspict,position="E")

    pspict.DrawGraphs(pts)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
