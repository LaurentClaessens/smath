# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *

class Pyramide(object):
    def __init__(self,n,l,h):
        """
        Une pyramide contenant 'n' rectangles à la base. 
        Ils ont une longueur 'l' et une hauteur 'h'.
        """
        self.rectangles=[]
        self.centres={}
        for i in range(0,n):
            y=i*h
            for j in range(0,n-i):
                x=j*l+i*(l/2)
                rect=Polygon(   Point(x,y),Point(x+l,y),Point(x+l,y-h),Point(x,y-h)  )
                self.rectangles.append(rect)
                self.centres[(j,i)]=Point(x+l/2,y-h/2)
    def bounding_box(self,pspict=None):
        return BasicGeometricObjects.BoundingBox()
    def action_on_pspict(self,pspict):
        pspict.DrawGraphs(self.rectangles)
        for P in self.centres.values():
            P.parameters.symbol="none"
            pspict.DrawGraphs(P)
    def latex_code(self,language=None,pspict=None):
        return ""

dilatation=1

def LYJooVYRkMy():
    pspict,fig = SinglePicture("LYJooVYRkMy")
    pspict.dilatation_X(dilatation)
    pspict.dilatation_Y(dilatation)

    x=var('x')
    pyramide=Pyramide(4,1,0.5)
    pyramide.centres[(0,0)].put_mark(0.0,0,"\( 1\)",automatic_place=(pspict,"center"))
    pyramide.centres[(1,0)].put_mark(0.0,0,"\( 1\)",automatic_place=(pspict,"center"))
    pyramide.centres[(2,0)].put_mark(0.0,0,"\( -1\)",automatic_place=(pspict,"center"))
    pyramide.centres[(3,0)].put_mark(0.0,0,"\( -1\)",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(pyramide)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def SCVooUjmESN():
    pspict,fig = SinglePicture("SCVooUjmESN")
    pspict.dilatation_X(dilatation)
    pspict.dilatation_Y(dilatation)

    x=var('x')
    pyramide=Pyramide(4,1,0.5)
    pyramide.centres[(0,0)].put_mark(0.0,0,"\( -2\)",automatic_place=(pspict,"center"))
    pyramide.centres[(1,0)].put_mark(0.0,0,"\( +2\)",automatic_place=(pspict,"center"))
    pyramide.centres[(2,0)].put_mark(0.0,0,"\( -2\)",automatic_place=(pspict,"center"))
    pyramide.centres[(3,0)].put_mark(0.0,0,"\( -2\)",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(pyramide)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def SWHooJzpmlM():
    SCVooUjmESN()
    LYJooVYRkMy()
