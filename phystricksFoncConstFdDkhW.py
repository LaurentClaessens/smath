# -*- coding: utf8 -*-
from phystricks import *
def FoncConstFdDkhW():
    pspict,fig = SinglePicture("FoncConstFdDkhW")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(1.5).graph(-3,3)

    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
