# -*- coding: utf8 -*-
from phystricks import *

def petit(x,y,color="lightgray"):
    color="lightgray"
    rect=Rectangle(  Point(x,y),Point(x+1,y+1) )
    rect.parameters.filled()
    rect.parameters.fill.color=color
    return rect

def contour(n,pspict):
    for k in range(0,n):      # Le haut et le bas
        pspict.DrawGraphs( petit(k,0,color="red"),petit(k,n-1,color="red") )
    for k in range(1,n-1):        # La gauche et la droite
        pspict.DrawGraphs( petit(0,k,color="green"),petit(n-1,k,color="green") )

def XYWooOPFwaca():
    pspict,fig = SinglePicture("XYWooOPFwaca")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    contour(3,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def BPZooBCyuyK():
    pspict,fig = SinglePicture("BPZooBCyuyK")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    contour(4,pspict)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def HVXooRtjPkd():
    XYWooOPFwaca()
    BPZooBCyuyK()
