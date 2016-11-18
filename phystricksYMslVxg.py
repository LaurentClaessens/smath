# -*- coding: utf8 -*-
from phystricks import *
def YMslVxg():
    pspict,fig = SinglePicture("YMslVxg")
    pspict.dilatation_X(0.4)
    pspict.dilatation_Y(0.4)

    xmin=-5
    xmax=5
    ymin=-5
    ymax=5

    x=var('x')
    F=[]
    F.append( phyFunction(-x+2).fit_inside(xmin,xmax,ymin,ymax) )  
    F.append( phyFunction(2).fit_inside(xmin,xmax,ymin,ymax) )  
    F.append( phyFunction(2*x-2).fit_inside(xmin,xmax,ymin,ymax) )  
    F.append( phyFunction(-x-2).fit_inside(xmin,xmax,ymin,ymax) )  

    F[0].put_mark(0.2,text="\( d_1\)",pspict=pspict,position="N")
    F[1].put_mark(0.2,text="\( d_2\)",pspict=pspict,position="W")
    F[2].put_mark(0.2,text="\( d_3\)",pspict=pspict,position="W")
    F[3].put_mark(0.2,text="\( d_4\)",pspict=pspict,position="N")

    pspict.DrawGraphs(F)
    pspict.axes.no_graduation()
    pspict.axes.single_axeX.put_mark(0.2,text="\( x\)",pspict=pspict,position="N")
    pspict.axes.single_axeY.put_mark(0.2,text="\( y\)",pspict=pspict,position="W")
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
