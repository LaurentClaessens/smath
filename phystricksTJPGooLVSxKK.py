# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def rect(a,b):
    return Polygon(  Point(a,0),Point(b,0),Point(b,1),Point(a,1)   )

def TJPGooLVSxKK():
    pspict,fig = SinglePicture("TJPGooLVSxKK")
    pspict.dilatation_X(6)
    pspict.dilatation_Y(1)

    rects=[]
    rects.append( rect(0,1/8) )
    rects.append( rect(1/8,2/8) )
    rects.append( rect(2/8,3/8) )
    rects.append( rect(3/8,1/2) )
    rects.append( rect(1/2,1) )

    for i in [0,1,2]:
        rects[i].parameters.hatched()
        rects[i].parameters.hatch.color='lightgray'

    pspict.DrawGraphs(rects)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
