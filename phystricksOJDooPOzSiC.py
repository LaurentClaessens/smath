# -*- coding: utf8 -*-
from phystricks import *
def OJDooPOzSiC():
    pspict,fig = SinglePicture("OJDooPOzSiC")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=4
    h=1
    rect=Rectangle(  Point(0,h),Point(l,0)   )
    rect.hatched()
    rect.hatch_parameters.color="lightgray"

    measurel=MeasureLength(  rect.edges[0] ,0.3  )
    measurel.put_mark(0.3,text="\( 2x+4\)",pspict=pspict,position="N")

    measureh=MeasureLength(  rect.edges[3] ,0.3  )
    measureh.put_mark(0.3,text="\( 5\)",pspict=pspict,position="E")

    pspict.DrawGraphs(rect,measurel,measureh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

