# -*- coding: utf8 -*-
from phystricks import *
def GraphInterfQVfSf():
    pspict,fig = SinglePicture("GraphInterfQVfSf")
    pspict.dilatation(1)

    x=var('x')
    f=LagrangePolynomial([Point(-3,-3),Point(-1,1),Point(1,-1),Point(5,2)]).graph(-3,5)
    A=f.get_point(-3)
    A.put_mark(0.2,-90,"\( A\)",pspict=pspict)
    B=f.get_point(5)
    B.put_mark(0.2,90,"\( B\)",pspict=pspict)

    pspict.DrawGraphs(A,B,f)
    pspict.DrawDefaultGrid()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
