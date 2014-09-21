# -*- coding: utf8 -*-
from phystricks import *
def KDtwIJf():
    pspict,fig = SinglePicture("KDtwIJf")
    pspict.dilatation_X(0.15)
    pspict.dilatation_Y(1)

    pspict.Mx_acceptable_BB=105

    minimum=0
    Maximum=100
    Q1=30
    mediane=55
    Q3=80
    moustache=Moustache(minimum,Q1,mediane,Q3,Maximum,h=0.5,delta_y=0.75)

    sm1=Segment(Point(minimum,0),Point(Q1,0))
    m1=MeasureLength(sm1,0.2)
    m1.put_mark(0.3,m1.advised_mark_angle,"Environ \( \\frac{ 1 }{ 4 }\)",automatic_place=pspict)

    sm2=Segment(Point(minimum,1.5),Point(Q3,1.5))
    m2=MeasureLength(sm2,0.2)
    m2.put_mark(-0.3,m2.advised_mark_angle,"Environ \( \\frac{ 3 }{ 4 }\)",automatic_place=pspict)

    sm3=Segment(Point(Q3,0),Point(Maximum,0))
    m3=MeasureLength(sm3,0.2)
    m3.put_mark(0.3,m3.advised_mark_angle,"Environ \( \\frac{ 1 }{ 4 }\)",automatic_place=pspict)

    pspict.DrawGraphs(moustache,m1,m2,m3)

    #pspict.DrawDefaultAxes()
    #pspict.axes.draw_single_axeY=False
    #pspict.axes.single_axeX.Dx=5
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
