# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def CFWIooWDSwRD():
    pspict,fig = SinglePicture("CFWIooWDSwRD")
    pspict.dilatation(0.3)

    O=Point(0,0)
    rayons=[2,3,4,5,6,7]
    cercles=[  Circle(O,r).graph(0*radian,2*pi*radian) for r in rayons  ]

    for i in range(len(rayons)-1):
        c1=cercles[i+1]
        c2=cercles[i]
        couronne=SurfaceBetweenParametricCurves(c2,c1,interval=(0,2*pi-0.001))
        couronne.parameters.filled()
        couronne.parameters.fill.color="white"
        if i%2==0:
            couronne.parameters.fill.color="lightgray"
        couronne.draw_Isegment=False
        couronne.draw_Fsegment=False
        pspict.DrawGraphs(couronne)

    A=Circle(O, (rayons[0]+rayons[1])/2 ).get_point(30)
    B=Circle(O, (rayons[2]+rayons[3])/2 ).get_point(120)
    C=Circle(O, (rayons[4]+rayons[5])/2 ).get_point(-90)
    
    O.put_mark(0.2,-45,"\( O\)",automatic_place=(pspict,"corner"))
    A.put_mark(0.2,30+90,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,120+90,"\( B\)",automatic_place=(pspict,"corner"))
    C.put_mark(0.2,-90+90,"\( C\)",automatic_place=(pspict,"W"))

    pspict.comment="Concentric grey filled circles."
    pspict.DrawGraphs(cercles,A,O,B,C)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
