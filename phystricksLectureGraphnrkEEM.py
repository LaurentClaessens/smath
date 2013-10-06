# -*- coding: utf8 -*-
from phystricks import *

# La fonction f est définie en dehors de la fonction LectureGraphnrkEEM parce qu'elle est importée depuis 
x=var('x')
f=phyFunction(-3*x**3/2 + 6*x**2/2 + 3*x/2 - 3/2).graph(-1,2.5)

def LectureGraphnrkEEM():
    pspict,fig = SinglePicture("LectureGraphnrkEEM")
    pspict.dilatation_X(2.5)
    pspict.dilatation_Y(0.7)

    pspict.axes.single_axeX.Dx=0.5
    pspict.DrawGraphs(f)
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
