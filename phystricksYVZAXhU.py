# -*- coding: utf8 -*-

from phystricks import *
from scipy import stats

def YVZAXhU():
    pspict,fig = SinglePicture("YVZAXhU")

    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(60)

    n=100
    p=0.16  # Ces nombres n et p sont en durs dans l'exemple du médecin dans le chapitre sur l'intervalle de confiance de 1stmg.
    mx=5
    Mx=29
    V=stats.binom(n,p)
    X=list(range(mx,Mx))
    Y=[V.pmf(k) for k in X]
    Bar=BarDiagram(X,Y)
    #Bar.numbering=False
    Bar.numbering_decimals=3
    Bar.lines_list[5-5].parameters.color="red"
    Bar.lines_list[6-5].parameters.color="red"
    Bar.lines_list[7-5].parameters.color="red"
    Bar.lines_list[8-5].parameters.color="red"

    Bar.lines_list[24-5].parameters.color="red"
    Bar.lines_list[25-5].parameters.color="red"
    Bar.lines_list[26-5].parameters.color="red"
    Bar.lines_list[27-5].parameters.color="red"
    Bar.lines_list[28-5].parameters.color="red"

    Bar.linewidth=0.3

    ax=SingleAxe(  Point(0,0),Vector(1,0), mx,Mx  )

    pspict.DrawGraphs(Bar,ax)
    #pspict.axes.single_axeX.Dx=5
    #pspict.axes.single_axeY.Dx=0.01
    #pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
