# -*- coding: utf8 -*-
from phystricks import *
def TJDooMNBjjK():
    pspict,fig = SinglePicture("TJDooMNBjjK")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    x=var('x')
    quadri=Polygon( Point(0,0),Point(4,0),Point(5,2),Point(2,2)  )

    pspict.DrawGraphs(quadri)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
