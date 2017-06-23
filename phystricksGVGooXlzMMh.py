# -*- coding: utf8 -*-

from __future__ import division
from sage.all import floor
from phystricks import *

def small_box(n,pc,pspict):
    x0=n*1.1
    rect=Rectangle( Point(x0,1),Point(  x0+1,0 ) )
    if n< floor(pc/10) :
        rect.filled()
        rect.fill_parameters.color="lightgray"
    pspict.DrawGraphs(rect)
    if n==floor(pc/10):
        reste=(pc-10*n)/10
        x1=x0+reste
        part=Rectangle(  Point(x0,1),Point(x1,0) )
        part.filled()
        part.fill_parameters.color="lightgray"
        pspict.DrawGraphs(part)

def GVGooXlzMMh():
    pspict,fig = SinglePicture("GVGooXlzMMh")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.5)

    pc=40
    for i in range(0,10):
        small_box(i,pc,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

