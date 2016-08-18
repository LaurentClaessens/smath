# -*- coding: utf8 -*-

from __future__ import division
from __future__ import unicode_literals
from phystricks import *

def NPGPooUwaiww():
    pspict,fig = SinglePicture("NPGPooUwaiww")
    pspict.dilatation(1)
    
    O=Point(0,0)
    mx=0
    Mx=6
    for i in range(0,4):
        P=Point(i,0)
        a=P.get_polar_point(0.1,90,pspict)
        b=P.get_polar_point(0.1,-90,pspict)
        pspict.DrawGraphs(Segment(a,b))

    axe=SingleAxe(O,Vector(1,0),mx,Mx,pspict=pspict)
    axe.no_graduation()

    Clerval=Point(0,0)
    Baume=Point(Mx/2,0)
    Besan=Point(Mx,0)

    Clerval.put_mark(0.2,-90,"Clerval",pspict=pspict,position="N")
    Baume.put_mark(0.2,-90,"Baume",pspict=pspict,position="N")
    Besan.put_mark(0.2,-90,"Besançon",pspict=pspict,position="N")
    Clerval.parameters.symbol=""
    Baume.parameters.symbol=""
    Besan.parameters.symbol=""

    pspict.DrawGraphs(axe,Clerval,Baume,Besan)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
