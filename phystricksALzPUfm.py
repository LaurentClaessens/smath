# -*- coding: utf8 -*-
from phystricks import *

def box(m,M,h):
    return Polygon( Point(m,0),Point(M,0),Point(M,h),Point(m,h) )

def ALzPUfm():
    pspict,fig = SinglePicture("ALzPUfm")
    pspict.dilatation_X(0.3)
    pspict.dilatation_Y(0.2)

    p1=box(0,4,0)
    p2=box(4,10,3)
    p3=box(10,11,12)
    p4=box(11,15,6)
    p5=box(15,17,8)
    p6=box(17,19,2)
    p7=box(19,29,1)

    pspict.DrawGraphs(p1,p2,p3,p4,p5,p6,p7)
    pspict.axes.draw_single_axeY=False
    pspict.axes.single_axeX.Dx=2
    pspict.axes.do_mx_enlarge=False
    pspict.axes.do_Mx_enlarge=False
    pspict.DrawDefaultAxes()
    #pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

