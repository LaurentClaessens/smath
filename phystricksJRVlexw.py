# -*- coding: utf8 -*-

from phystricks import *
from scipy import stats

def JRVlexw():
    pspict,fig = SinglePicture("JRVlexw")
    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(50)

    n=100
    p=0.16  # Ces nombres n et p sont en durs dans l'exemple du médecin dans le chapitre sur l'intervalle de confiance de 1stmg.
    V=stats.binom(n,p)
    X=list(range(5,30))
    Y=[V.pmf(k) for k in X]
    Bar=BarDiagram(X,Y)
    Bar.linewidth=0.3

    pspict.DrawGraphs(Bar,Bar.bounding_box(pspict))
    #pspict.axes.single_axeX.Dx=5
    #pspict.axes.single_axeY.Dx=0.01
    #pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
