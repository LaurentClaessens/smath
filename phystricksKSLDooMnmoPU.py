# -*- coding: utf8 -*-
from phystricks import *
def KSLDooMnmoPU():
    pspict,fig = SinglePicture("KSLDooMnmoPU")
    pspict.dilatation(0.7)

    A=Point(4,0)
    B=Point(1.5,3)
    C=Point(0,0)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspict)

    hauteur=triangle.edges[1].orthogonal_trough(A).dilatation(1.3)
    hauteur.parameters.style="dashed"
    L=Intersection(hauteur,triangle.edges[1])[0]
    L.put_mark(0.3,45,"\( L\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(triangle,hauteur,L)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
