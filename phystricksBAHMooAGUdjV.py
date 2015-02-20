# -*- coding: utf8 -*-
from phystricks import *
def BAHMooAGUdjV():
    pspict,fig = SinglePicture("BAHMooAGUdjV")
    pspict.dilatation(1)
    
    A=Point(0,0)
    B=Point(0,-2)
    C=Point(3,0)

    trig=Polygon(A,B,C)
    trig.put_mark(0.5,pspict=pspict)

    rh=RightAngle(trig.edges[0],trig.edges[2],0.3,1,0)

    no_symbol(trig.vertices)

    pspict.DrawGraphs(trig,rh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
