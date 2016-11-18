# -*- coding: utf8 -*-

import string
from phystricks import *

def NGWKooMCeSDk():
    pspict,fig = SinglePicture("NGWKooMCeSDk")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(1)

    O=Point(0,0)
    O.put_mark(0.2,text="\( O\)",pspict=pspict,position="N")
    O.parameters.symbol=''

    points=[   Point(x,0) for x in [-3,-1,3,5]  ]
    mx=min([  P.x for P in points ])
    Mx=max([  P.x for P in points ])
    
    for i in range(0,len(points)):
        P=points[i]
        P.parameters.symbol=''
        P.put_mark(0.2,text=pspict=pspict,position="N")

    axe=SingleAxe(O,Vector(1,0),mx-2,Mx+2,pspict=pspict)
    axe.no_numbering()

    pspict.DrawGraphs(O,axe,points)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
