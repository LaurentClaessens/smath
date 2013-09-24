# -*- coding: utf8 -*-
from phystricks import *
def AZKoIsL():
    pspict,fig = SinglePicture("AZKoIsL")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(0.6)

    # Je ne fais pas la fonction g parce que le dessin est alors trop chargé.

    f=phyFunction((x+2)**2-1).graph(-4,0) 
    #g=-HermiteInterpolation( [(-3,0,-1),(-2,-1,0),(0,2,0),(1,0,0)] ).graph(-3,1.3)  
    h=HermiteInterpolation([(-4,-2,0),(-1,1,0),(2,-1,0)]).graph(-4.5,4) 

    f.put_mark(0.2,0,"\( f\)",automatic_place=(pspict,"W"))
    #g.put_mark(0.2,0,"\( g\)",automatic_place=(pspict,"W"))
    h.put_mark(0.2,0,"\( h\)",automatic_place=(pspict,"W"))

    f.parameters.color="blue"
    h.parameters.color="brown"

    #pspict.DrawGraphs(f,g,h)
    pspict.DrawGraphs(f,h)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
