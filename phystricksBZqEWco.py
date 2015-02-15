# -*- coding: utf8 -*-
from phystricks import *
def BZqEWco():
    pspict,fig = SinglePicture("BZqEWco")

    pspict.dilatation_X(0.7)
    pspict.dilatation_Y(0.7)

    x=var('x')
    f=phyFunction(x-2).graph(-2,4)

    B=f.get_point(0)
    B.put_mark(0.2,None,"\( p\)",automatic_place=pspict)
        
    x0=solve(f(x)==0,x)[0].rhs()
    A=f.get_point(x0)
    A.put_mark(0.2,None,"\( -p/m\)",automatic_place=pspict)
        
    pspict.DrawGraphs(f,A,B)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
