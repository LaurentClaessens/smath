# -*- coding: utf8 -*-
from phystricks import *
def NPGPooUwaiww():
    pspict,fig = SinglePicture("NPGPooUwaiww")
    pspict.dilatation(1)
    
    mx=0
    Mx=6
    for i in range(0,4):
        P=Point(i,0)
        a=visual_polar(P,0.1,bar_angle,pspict)
        b=visual_polar(P,0.1,bar_angle+180,pspict)
        pspict.DrawGraphs(Segment(a,b))


    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    axe.no_graduation()

    pspict.DrawGraphs(axe)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
