# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *
from scipy import stats

def GCxOEgb():
    pspict,fig = SinglePicture("GCxOEgb")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(30)

    n=30
    p=0.91  
    X=stats.binom(n,p)

    w=0.3
    mx=21
    Mx=32
    for i in range(mx,Mx):
        h=X.pmf(i)
        seg=Segment(  Point(i,0),Point(i,h)  )
        seg.parameters.color="blue"
        seg.parameters.add_option("linewidth","{}cm".format(w))
        P=Point( i,h )
        P.parameters.symbol=""
        P.put_mark(0.2,text="\( {:.3f}\)".format(h),pspict=pspict,position="S")
        Q=Point(i,0)
        Q.put_mark(0.2,angle=-90,added_angle=0,text="\( {}\)".format(i),pspict=pspict)
        Q.parameters.symbol=""
        pspict.DrawGraphs(seg,P,Q)

    ax=AffineVector( Point(mx-1,0),Point(Mx+1,0)  )
    pspict.DrawGraphs(ax)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
