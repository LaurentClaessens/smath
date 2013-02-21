# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *
from scipy import stats

def GCxOEgb():
    pspict,fig = SinglePicture("GCxOEgb")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(60)

    n=30
    p=0.36  # Ces nombres n et p sont en durs dans l'énoncé de l'exercice exosmath-0384.tex
    X=stats.binom(n,p)

    w=0.3
    for i in range(0,21):
        h=X.pmf(i)
        seg=Segment(  Point(i,0),Point(i,h)  )
        seg.parameters.color="blue"
        seg.parameters.add_option("linewidth","{}cm".format(w))
        P=Point( i,h )
        P.parameters.symbol="none"
        P.put_mark(0.2,90,"\( {:.3f}\)".format(h),automatic_place=(pspict,"S"))
        pspict.DrawGraphs(seg,P)

    pspict.axes.single_axeY.Dx=0.01
    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
