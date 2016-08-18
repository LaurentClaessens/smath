# -*- coding: utf8 -*-
from phystricks import *
def POYHooNCayFj():
    pspict,fig = SinglePicture("POYHooNCayFj")
    pspict.dilatation(1)

    O=Point(0,0)
    vA=Vector(1,2)
    vB=Vector(2,1)
    A=O+vA
    B=O+3*vA
    C=O+vB
    D=O+3*vB

    s1=Segment(O,B)
    s2=Segment(O,D)
    p1=Segment(A,C)
    p2=Segment(B,D)

    p1.put_mark(0.2,angle=None,added_angle=0,text="\( a\)",pspict=pspict)
    p2.put_mark(0.2,angle=None,added_angle=0,text="?",pspict=pspict)

    pspict.DrawGraphs(s1,s2,p1,p2)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

