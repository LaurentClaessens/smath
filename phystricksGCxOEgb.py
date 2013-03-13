# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *
from scipy import stats

def GCxOEgb():
    pspict,fig = SinglePicture("GCxOEgb")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(30)

    n=30
    p=0.91  
    X=stats.binom(n,p)

    w=0.3
    mx=18
    Mx=30
    for i in range(mx,Mx):
        h=X.pmf(i)
        seg=Segment(  Point(i,0),Point(i,h)  )
        seg.parameters.color="blue"
        seg.parameters.add_option("linewidth","{}cm".format(w))
        P=Point( i,h )
        P.parameters.symbol="none"
        P.put_mark(0.2,90,"\( {:.3f}\)".format(h),automatic_place=(pspict,"S"))
        pspict.DrawGraphs(seg,P)

    ax=SingleAxe(  Point(0,0),Vector(1,0), mx,Mx  )
    pspict.DrawGraphs(ax)
    fig.conclude()
    fig.write_the_file()
