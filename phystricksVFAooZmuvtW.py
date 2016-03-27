# -*- coding: utf8 -*-
from phystricks import *
def VFAooZmuvtW():
    pspict,fig = SinglePicture("VFAooZmuvtW")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(0.5)

    mx=-3
    Mx=7

    x=var('x')
    F=[]
    F.append(phyFunction((x+2)/(2*x-6)).graph(mx,Mx))

    for f in F:
        f.cut_y(-8,8)

    import random
    random.shuffle(F)

    pspict.DrawGraphs(F)
    #pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    pspict.comment="An homographic function cutted at $y$ between $-8$ and $8$"

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
