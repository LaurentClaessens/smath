# -*- coding: utf8 -*-
from phystricks import *
def QZPMooIiOQpy():
    pspicts,figs = IndependentPictures("QZPMooIiOQpy",2)
    for psp in pspicts :
        psp.dilatation(1)

    A=Point(0,0)
    B=Point(4,1)
    C=Point(2.5,3)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspict=pspicts)
    for psp in pspicts:
        psp.DrawGraphs(triangle)
    
    for i in [0,1,2]:
        P=triangle.vertices[i]
        cot=triangle.edges[ (i+1)%3 ]
        hauteur=cot.orthogonal_trough(P).dilatation(1.5)
        hauteur.parameters.style="dashed"
        rh=RightAngle(hauteur,cot,0,0)
        pspicts[0].DrawGraphs(hauteur)
        pspicts[1].DrawGraphs(hauteur,rh)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
