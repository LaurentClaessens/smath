# -*- coding: utf8 -*-

import string
from phystricks import *

def carre(x,y,color=None):
    car=Polygon(  Point(x,y),Point(x+1,y),Point(x+1,y+1),Point(x,y+1)  )
    if color:
        car.parameters.filled()
        car.parameters.fill.color=color
    return car

def PYSIooVNiiuo():
    pspict,fig = SinglePicture("PYSIooVNiiuo")
    pspict.dilatation(0.5)

    for i in range(0,4):
        P=Point(i+0.5,0)
        Q=Point(0,i+0.5)
        P.put_mark(0.2,angle=-90,added_angle=0,text=str(i+1),pspict=pspict)
        Q.put_mark(0.2,angle=180,added_angle=0,text=string.ascii_letters[3-i],pspict=pspict)
        no_symbol(P,Q)
        pspict.DrawGraphs(P,Q)
        for j in range(0,4):
            car=carre(i,j)
            pspict.DrawGraphs(car)
    blocs=[]
    blocs.append(carre(0,0))
    blocs.append(carre(2,0))
    blocs.append(carre(1,1))
    blocs.append(carre(3,2))
    blocs.append(carre(2,3))
    for b in blocs:
        b.parameters.filled()
        b.parameters.fill.color="black"
    
    pspict.DrawGraphs(blocs)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
