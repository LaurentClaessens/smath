# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

c=0.3
def small_box(X,Y,pspict,text=""):
    x=c*X
    y=c*Y
    A=Point(x-c/2,y-c/2)
    B=Point(x+c/2,y-c/2)
    C=Point(x+c/2,y+c/2)
    D=Point(x-c/2,y+c/2)
    P=Point(x,y)
    P.put_mark(0.0,0,text,automatic_place=pspict)
    P.parameters.symbol="none"
    return [P,Polygon(A,B,C,D)]

def WGhpCVm():
    pspict,fig = SinglePicture("WGhpCVm")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    Q=[]
    Q.append(small_box(1,1),pspict)
    Q.append(small_box(2,1),pspict)
    Q.append(small_box(3,1),pspict)
    Q.append(small_box(4,1),pspict)
    Q.append(small_box(1,2),pspict)
    Q.append(small_box(2,2),pspict)
    Q.append(small_box(3,2),pspict)
    Q.append(small_box(1,3),pspict)
    Q.append(small_box(2,3),pspict)
    Q.append(small_box(1,4),pspict)

    pspict.DrawGraphs(  [q[1] for q in Q]  )
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
