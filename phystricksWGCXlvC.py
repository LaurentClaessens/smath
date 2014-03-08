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
    F[0].put_mark(0.2,180,"\( d_1\)",mark_point=F[0].I,automatic_place=(pspict,"N"))
    F[1].put_mark(0.2,0,"\( d_2\)",mark_point=F[1].F,automatic_place=(pspict,"W"))
    F[2].put_mark(0.2,0,"\( d_3\)",mark_point=F[2].F,automatic_place=(pspict,"W"))
    F[3].put_mark(0.2,180,"\( d_4\)",mark_point=F[3].I,automatic_place=(pspict,"N"))

    pspict.DrawGraphs(F)
    pspict.axes.no_graduation()
    pspict.axes.single_axeX.put_mark(0.2,-90,"\( x\)",automatic_place=(pspict,"N"))
    pspict.axes.single_axeY.put_mark(0.2,0,"\( y\)",automatic_place=(pspict,"W"))
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
