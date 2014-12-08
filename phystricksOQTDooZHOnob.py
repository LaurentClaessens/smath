# -*- coding: utf8 -*-
from phystricks import *
def OQTDooZHOnob():
    pspict,fig = SinglePicture("OQTDooZHOnob")
    pspict.dilatation(1)
    
    A=Point(0,0)
    B=Circle(A,6).get_point(90)
    C=Circle(A,3).get_point(30)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)

    pspict.DrawGraphs(triangle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
