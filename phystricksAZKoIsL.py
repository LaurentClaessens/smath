# -*- coding: utf8 -*-
from phystricks import *
def AZKoIsL():
    pspict,fig = SinglePicture("AZKoIsL")
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(0.6)

    # Je ne fais pas la fonction g parce que le dessin est alors trop chargé.
    # Si un jour on remet une fonction ou qu'on en change le nom,
    # il faudra changer le texte dans la question.

    x=var('x')
    f=phyFunction((x+2)**2-1).graph(-4,0) 
    #h=-HermiteInterpolation( [(-3,0,-1),(-2,-1,0),(0,2,0),(1,0,0)] ).graph(-3,1.3)  
    g=HermiteInterpolation([(-4,-2,0),(-1,1,0),(2,-1,0)]).graph(-4.5,4) 

    f.put_mark(0.2,0,"\( f\)",pspict=pspict,position="W")
    #h.put_mark(0.2,0,"\( h\)",pspict=pspict,position="W")
    g.put_mark(0.2,0,"\( g\)",pspict=pspict,position="W")

    f.parameters.color="blue"
    g.parameters.color="brown"

    #pspict.DrawGraphs(f,g,h)
    pspict.DrawGraphs(f,g)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
