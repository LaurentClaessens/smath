# -*- coding: utf8 -*-
from phystricks import *
def YMslVxg():
    pspict,fig = SinglePicture("YMslVxg")
    pspict.dilatation_X(0.6)
    pspict.dilatation_Y(0.6)

    xmin=-5
    xmax=5
    ymin=-5
    ymax=5

    F=[]
    F.append( phyFunction(-x+2).fit_inside(xmin,xmax,ymin,ymax) )  
    F.append( phyFunction(2).fit_inside(xmin,xmax,ymin,ymax) )  
    F.append( phyFunction(2*x-2).fit_inside(xmin,xmax,ymin,ymax) )  
    F.append( phyFunction(-x-2).fit_inside(xmin,xmax,ymin,ymax) )  

    X=Point(  F[2].Mx,F[2].sage(F[2].Mx))
    X.put_mark(0.2,0,"\( X\)",automatic_place=(pspict,"W"))

    F[0].put_mark(0.2,180,"\( d_1\)",automatic_place=(pspict,"N"))
    F[1].put_mark(0.2,0,"\( d_2\)",automatic_place=(pspict,"W"))
    F[2].put_mark(0.2,0,"\( d_3\)",mark_point=Point(  F[2].Mx,F[2].sage(F[2].Mx)  ),automatic_place=(pspict,"W"))
    F[3].put_mark(0.2,180,"\( d_4\)",automatic_place=(pspict,"N"))

    pspict.DrawGraphs(F,X)
    pspict.axes.no_graduation()
    pspict.axes.single_axeX.put_mark(0.2,-90,"\( x\)",automatic_place=(pspict,"N"))
    pspict.axes.single_axeY.put_mark(0.2,0,"\( y\)",automatic_place=(pspict,"W"))
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
