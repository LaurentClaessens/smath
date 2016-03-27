# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def f1(x):
    if x <= 7:
        return 150
    return 150+25*(x-7)

def f2(x):
    return 30*x

def f3(x):
    return 50+25*x

def liste_morceaux(f,mx,Mx):
    l=[]
    for i in range(mx,Mx):
        l.append(Point(i,f(i)))
        l.append(Point(i,f(i+1)))
    s=[ Segment( l[i],l[i+1] ) for i,s in enumerate(l) if i != len(l)-1 ]
    return s

def figureHYeBZVj():
    pspict,fig = SinglePicture("figureHYeBZVj")
    pspict.dilatation_Y(1/50)
    pspict.My_acceptable_BB=600
    #pspict.my_acceptable_BB=-600

    Mx=13
    s1=liste_morceaux(f1,1,Mx)
    s2=liste_morceaux(f2,1,Mx)
    s3=liste_morceaux(f3,1,Mx)

    for seg in s1:
        seg.parameters.color="red"
    for seg in s2:
        seg.parameters.color="brown"
        seg.parameters.style="dashed"
    for seg in s3:
        seg.parameters.color="blue"
        seg.parameters.style="dashed"

    pspict.DrawGraphs(s1,s2,s3)
    pspict.axes.single_axeY.Dx=50
    pspict.grid.Dx=1
    pspict.grid.Dy=25
    pspict.grid.num_subX=0
    pspict.grid.num_subY=1
    pspict.axes.do_mx_enlarge=False
    pspict.axes.do_my_enlarge=False
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.conclude()
    fig.write_the_file()

    pspict.comment="This picture displays large numbers, but remains reasonably small."
