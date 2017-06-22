# -*- coding: utf8 -*-
from phystricks import *
def LXQooZPbZml():
    pspict,fig = SinglePicture("LXQooZPbZml")
    pspict.dilatation(0.7)

    grand=Polygon(  Point(0,0),Point(4,0),Point(4,4),Point(0,4) )
    moyen=Polygon( Point(0,0),Point(2,0),Point(2,2),Point(0,2)   )

    petit1=Rectangle( Point(0,2),Point(1,3) )
    petit2=Rectangle( Point(1,2),Point(2,3) )
    petit3=Rectangle( Point(0,3),Point(1,4) )

    petit1.filled()
    petit1.fill_parameters.color="lightgray"
    petit2.filled()
    petit2.fill_parameters.color="lightgray"
    petit3.filled()
    petit3.fill_parameters.color="lightgray"

    moyen.hatched()
    moyen.hatch_parameters.color="lightgray"

    pspict.DrawGraphs(grand,moyen,petit1,petit2,petit3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
