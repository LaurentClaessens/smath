# -*- coding: utf8 -*-
from phystricks import *
def WGCXlvC():
    pspict,fig = SinglePicture("WGCXlvC")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(0.6)

    xmin=-5
    xmax=5
    ymin=-5
    ymax=5

    F=[]
    F.append(Segment(   Point(0,2),Point(1,4)  ))   # 2x+2
    F.append(Segment(   Point(0,-2),Point(1,0)  ))
    F.append(Segment(   Point(0,0),Point(1,3)  ))
    F.append(Segment(   Point(0,2),Point(1,0)  ))

    F=[ f.fit_inside(xmin,xmax,ymin,ymax) for f in F]
    F[0].put_mark(0.2,text="\( d_1\)",mark_point=F[0].I,pspict=pspict,position="N")
    F[1].put_mark(0.2,text="\( d_2\)",mark_point=F[1].F,pspict=pspict,position="W")
    F[2].put_mark(0.2,text="\( d_3\)",mark_point=F[2].F,pspict=pspict,position="W")
    F[3].put_mark(0.2,text="\( d_4\)",mark_point=F[3].I,pspict=pspict,position="N")

    pspict.DrawGraphs(F)
    pspict.axes.no_graduation()
    pspict.axes.single_axeX.put_mark(0.2,text="\( x\)",pspict=pspict,position="N")
    pspict.axes.single_axeY.put_mark(0.2,text="\( y\)",pspict=pspict,position="W")
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
