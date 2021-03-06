# -*- coding: utf8 -*-
from phystricks import *

def petit(x,y,color=0):
    # color=0 donne un carré vide
    #  1 donne remplit et 2 donne hachuré
    rect=Rectangle(  Point(x,y),Point(x+1,y+1) )
    if color==0:
        return rect
    if color==1:
        rect.filled()
        rect.fill_parameters.color="lightgray"
        return rect
    rect.hatched()
    rect.hatch_parameters.color="lightgray"
    return rect

def CMUTooFyLisx():
    pspict,fig = SinglePicture("CMUTooFyLisx")
    pspict.dilatation(0.4)

    h=10
    L=20

    for i in range(0,L):
        for j in range(0,h):
            pspict.DrawGraphs(petit(i,j))
    pspict.DrawGraphs( petit(0,0,color=1),petit(L-1,h-1,color=1) )
    pspict.DrawGraphs( petit(L-1,0,color=1),petit(0,h-1,color=1) )

    x=4
    for i in range(0,x):
        p1= petit(i,4,color=2)  
        p2= petit(i,5,color=2)  
        p3= petit(L-1-i,4,color=2)  
        p4= petit(L-1-i,5,color=2)  
        pspict.DrawGraphs(p1,p2,p3,p4)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
