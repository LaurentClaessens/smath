# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *
from phystricks.ObjectGraph import ObjectGraph

class Pyramide(ObjectGraph):
    def __init__(self,n,l,h):
        """
        Une pyramide contenant 'n' rectangles à la base. 
        Ils ont une longueur 'l' et une hauteur 'h'.
        """
        ObjectGraph.__init__(self,self)
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
    def math_bounding_box(self,pspict=None):
        return self.bounding_box(pspict)
    def action_on_pspict(self,pspict):
        pspict.DrawGraphs(self.rectangles)
        for P in self.centres.values():
            P.parameters.symbol=""
            pspict.DrawGraphs(P)
    def latex_code(self,language=None,pspict=None):
        return ""

def DS_statistics(moustaches,pspict):
    pspict.dilatation_X(0.8)
    pspict.dilatation_Y(1)

    #for i,m in enumerate(moustaches) :
    #    m.delta_y=0.75+i
    #    m.put_mark(0.2,0,"DS {}".format( len(moustaches)-i ),pspict=pspict,position="W")
    for i,m in enumerate(moustaches) :
        m.delta_y=len(moustaches)+0.75-i-1
        m.put_mark(0.2,0,"DS {}".format( i+1 ),pspict=pspict,position="W")

    maxy=len(moustaches)
    ledix=Segment(  Point(10,0),Point(10,maxy)   )
    ledix.parameters.color="green"
    ledix.parameters.linewidth=2
    ledix.parameters.style="dashed"

    pspict.DrawGraphs(moustaches,ledix)
    pspict.grid.draw_horizontal_grid=False
    pspict.axes.draw_single_axeY=False
    pspict.axes.single_axeY.no_graduation()
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
