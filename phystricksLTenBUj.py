# -*- coding: utf8 -*-
from phystricks import *
def LTenBUj():
    pspict,fig = SinglePicture("LTenBUj")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    H=Histogram([(0,0.25,137),(0.25,0.5,106),(0.5,1,112),(1,2.5,154),(2.5,5,100),(5,10,33)])
    H.legende="Chiffre d'affaires (en millions d'euros)"

    pspict.DrawGraphs(H)
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
