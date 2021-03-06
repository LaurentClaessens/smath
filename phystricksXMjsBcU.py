# -*- coding: utf8 -*-
from phystricks import *
def XMjsBcU():
    pspict,fig = SinglePicture("XMjsBcU")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(0.5)

    x=var('x')
    mx=-1.5
    Mx=2
    f=phyFunction(-2*x+3).graph(mx,Mx)
    f.put_mark(0.2,text="\( d_1\)",mark_point=f.get_point(mx),pspict=pspict,position="S")

    pspict.DrawGraphs(f)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
