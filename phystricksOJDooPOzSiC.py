# -*- coding: utf8 -*-
from phystricks import *
def OJDooPOzSiC():
    pspict,fig = SinglePicture("OJDooPOzSiC")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=4
    h=1
    rect=Rectangle(  Point(0,h),Point(l,0)   )
    rect.parameters.hatched()
    rect.parameters.hatch.color="lightgray"

    measurel=MeasureLength(  rect.edges[0] ,0.3  )
    measurel.put_mark(0.3,-90,"\( 2x+4\)",automatic_place=(pspict,"N"))

    measureh=MeasureLength(  rect.edges[3] ,0.3  )
    measureh.put_mark(0.3,180,"\( 5\)",automatic_place=(pspict,"E"))

    pspict.DrawGraphs(rect,measurel,measureh)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

