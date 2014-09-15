# -*- coding: utf8 -*-
from phystricks import *
def LXQooZPbZml():
    pspict,fig = SinglePicture("LXQooZPbZml")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    grand=Polygon(  Point(0,0),Point(4,0),Point(4,4),Point(0,4) )
    moyen=Polygon( Point(0,0),Point(2,0),Point(2,2),Point(0,2)   )

    petit1=Rectangle( Point(0,2),Point(1,3) )
    petit2=Rectangle( Point(1,2),Point(2,3) )
    petit3=Rectangle( Point(0,3),Point(1,4) )

    petit1.parameters.filled()
    petit1.parameters.fill.color="lightgray"
    petit2.parameters.filled()
    petit2.parameters.fill.color="lightgray"
    petit3.parameters.filled()
    petit3.parameters.fill.color="lightgray"

    moyen.parameters.hatched()
    petit3.parameters.hatch.color="lightgray"

    pspict.DrawGraphs(grand,moyen,petit1,petit2,petit3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
