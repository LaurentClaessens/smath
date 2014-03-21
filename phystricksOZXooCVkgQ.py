# -*- coding: utf8 -*-
from phystricks import *
def OZXooCVkgQ():
    pspict,fig = SinglePicture("OZXooCVkgQ")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    H=Histogram([(0,5,2),(5,8,7),(8,10,10),(10,12,12),(12,15,1),(15,20,1)])
    H.legende=u"Les notes à un devoir"

    pspict.DrawGraphs(H)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
