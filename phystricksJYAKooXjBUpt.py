# -*- coding: utf8 -*-
from phystricks import *
def JYAKooXjBUpt():
    pspicts,figs = IndependentPictures("JYAKooXjBUpt",3)

    l1=3
    l2=4
    l3=5
    h=2

    A=Point(0,0)
    B=A+(l1,0)
    c1=Circle(A,l3)
    c2=Circle(B,l2)
    C=Intersection(c1,c2)[1]

    trig=Polygon(A,B,C)

    for psp in pspicts:
        psp.dilatation(1)

    <+Définition des objets+>

    for psp in pspicts:
        psp.DrawDefaultAxes()

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
