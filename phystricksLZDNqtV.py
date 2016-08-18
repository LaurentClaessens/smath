# -*- coding: utf8 -*-
from phystricks import *
def LZDNqtV():
    pspict,fig = SinglePicture("LZDNqtV")
    #pspict.dilatation_X(0.02)
    #pspict.dilatation_Y(0.02)
    pspict.dilatation(0.02)

    O=Point(0,0)
    h=56
    r=65
    sphere=Circle(O,r)
    plan=Segment( Point(-r,h),Point(r,h) ).dilatation(1.3)
    C=Point(0,h)

    intersections=Intersection(sphere,plan)
    I=intersections[1]
    rayon=Segment(O,I)

    C.put_mark(0.2,90,"\( C\)",pspict=pspict,position="S")
    I.put_mark(0.2,45,"\( I\)",pspict=pspict)
    O.put_mark(0.2,-90,"\( O\)",pspict=pspict,position="N")

    pspict.DrawGraphs(sphere,plan,rayon,C,I,rayon,O)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
