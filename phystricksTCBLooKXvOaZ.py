# -*- coding: utf8 -*-
from phystricks import *

def petit(x,y,color="lightgray",filled=True):
    color="lightgray"
    rect=Rectangle(  Point(x,y),Point(x+1,y+1) )
    if filled :
        rect.parameters.filled()
        rect.parameters.fill.color=color
    return rect

def contour(n,pspict):
    for k in range(1,n-1):      # Le haut et le bas
        pspict.DrawGraphs( petit(k,0,color="red"),petit(k,n-1,color="red") )
    for k in range(1,n-1):        # La gauche et la droite
        pspict.DrawGraphs( petit(0,k,color="green"),petit(n-1,k,color="green") )

def grand(n,pspict):
    for k in range(0,n):   
        for l in range(0,n):
            pspict.DrawGraphs( petit(k,l,color="cyan",filled=False))


def TCBLooKXvOaZ():
    pspict,fig = SinglePicture("TCBLooKXvOaZ")
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    grand(5,pspict)
    contour(5,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
