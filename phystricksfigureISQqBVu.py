# -*- coding: utf8 -*-
from phystricks import *
def figureISQqBVu():
    pspict,fig = SinglePicture("figureISQqBVu")
    pspict.dilatation(0.7)

    al=Rectangle(xmin=0,xmax=4,ymin=0,ymax=4)
    parc=Rectangle(xmin=1,xmax=3,ymin=1,ymax=3)

    parc.hatched()

    A=Point(3,4)
    B=Point(4,4)
    seg=Segment(B,A)
    measure=MeasureLength(seg,0.2)
    measure.put_mark(0.2,90,"\( x\)",pspict=pspict)

    pspict.DrawGraphs(al,parc,measure)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
