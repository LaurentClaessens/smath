# -*- coding: utf8 -*-
from phystricks import *
def figurePQKzIRY():
    pspict,fig = SinglePicture("figurePQKzIRY")
    pspict.dilatation(0.3)

    r1=Rectangle(xmin=0,ymin=2,xmax=6,ymax=9)
    r2=Rectangle(xmin=6,ymin=6,xmax=9,ymax=9)
    r3=Rectangle(xmin=6,ymin=3,xmax=9,ymax=6)
    r4=Rectangle(xmin=6,ymin=0,xmax=9,ymax=3)
    r5=Rectangle(xmin=0,ymin=0,xmax=2,ymax=2)
    r6=Rectangle(xmin=2,ymin=0,xmax=4,ymax=2)
    r7=Rectangle(xmin=4,ymin=0,xmax=6,ymax=2)

    r1.parameters.hatched()

    pspict.DrawGraphs(r1,r2,r3,r4,r5,r6,r7)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

