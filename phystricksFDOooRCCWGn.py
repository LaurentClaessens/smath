# -*- coding: utf8 -*-
from phystricks import *

def petit(x,y):
    return Rectangle(  Point(x,y+1),Point(x+1,y) )

def FDOooRCCWGn():
    pspict,fig = SinglePicture("FDOooRCCWGn")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(0.7)

    l=7
    h=3

    for i in range(0,l):
        for j in range(0,h):
            pet=petit(i,j)
            pspict.DrawGraphs(pet)
    pet=petit(0,h-1)
    pet.parameters.filled()
    pet.parameters.fill.color='lightgray'

    s1=Segment( Point(0,h),Point(l,h) )
    s1.parameters.color='red'
    s2=Segment( Point(0,h),Point(0,0) )
    s2.parameters.color='green'


    measure1=MeasureLength(  s1 ,-0.3  )
    measure1.put_mark(0.3,90,"\SI{10}{\centi\meter}",automatic_place=(pspict,"S"))
    measure2=MeasureLength(  s2 ,0.3  )
    measure2.put_mark(0.3,180,"\SI{4}{\centi\meter}",automatic_place=(pspict,"E"))

    pspict.DrawGraphs(pet,measure1,measure2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
