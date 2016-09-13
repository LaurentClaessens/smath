# -*- coding: utf8 -*-
from phystricks import *
def IRQOooJMDFdv():
    pspicts,figs = IndependentPictures("IRQOooJMDFdv",3)

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)

    A=Point(0,0)
    B=Point(3,-1)
    C=Point(5,2)

    triangle=Polygon(A,B,C)
    triangle.put_mark(0.2,pspicts=pspicts)
    mediatrice=triangle.edges[1].bisector().dilatation(1.5)
    hauteur=triangle.edges[1].orthogonal_trough(A).dilatation(1.5)
    mediane=Segment(  triangle.vertices[2],triangle.edges[0].midpoint()  ).dilatation(1.5)

    for psp in pspicts:
        psp.DrawGraphs(triangle)


    pspicts[1].DrawGraphs(mediatrice)
    pspicts[2].DrawGraphs(mediane)

    triangle.edges[0].divide_in_two(n=1,d=0.1,l=0.2,angle=45,pspicts=pspicts)
    triangle.edges[1].divide_in_two(n=2,d=0.1,l=0.2,angle=45,pspicts=pspicts)

    prolongation=Segment(C,B).add_size(lF=1)
    prolongation.parameters.style="dotted"
    rh=RightAngle(prolongation,hauteur,0,0)
    mediatrice2=triangle.edges[2].bisector().dilatation(1.5)

    pspicts[0].DrawGraphs(mediatrice,hauteur,mediane,prolongation,rh,mediatrice2)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
