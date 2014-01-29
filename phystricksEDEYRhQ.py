# -*- coding: utf8 -*-

from __future__ import division
from __future__ import unicode_literals
from phystricks import *

def EDEYRhQ():
    pspict,fig = SinglePicture("EDEYRhQ")
    pspict.dilatation_X(1/6)
    pspict.dilatation_Y(1)

    BasicGeometricObjects.GraphOfASegment.mark_point=lambda x:x.center()

    l1=10
    l2=15
    l3=9
    l4=9
    l5=12

    x=var('x')
    A=Point(-4,0)
    B=Point(6,0)
    C=Point(21,0)
    D=Point(30,0)
    E=Point(39,0)
    F=Point(51,0)

    A.put_mark(0.2,-90,"Besançon",automatic_place=(pspict,"N"))
    B.put_mark(0.2,-90,"St-Vit",automatic_place=(pspict,"N"))
    C.put_mark(0.2,-90,"Dole",automatic_place=(pspict,"N"))
    D.put_mark(0.2,-90,"Auxonne",automatic_place=(pspict,"N"))
    E.put_mark(0.2,-90,"Genlis",automatic_place=(pspict,"N"))
    F.put_mark(0.2,-90,"Dijon",automatic_place=(pspict,"N"))

    AB=AffineVector(A,B)
    AB.put_mark(0.2,90,"\( {}\)".format(B.x-A.x),automatic_place=(pspict,"S"))
    BC=AffineVector(B,C)
    BC.put_mark(0.2,90,"\( {}\)".format(C.x-B.x),automatic_place=(pspict,"S"))
    CD=AffineVector(C,D)
    CD.put_mark(0.2,90,"\( {}\)".format(D.x-C.x),automatic_place=(pspict,"S"))
    DE=AffineVector(D,E)
    DE.put_mark(0.2,90,"\( {}\)".format(E.x-D.x),automatic_place=(pspict,"S"))
    EF=AffineVector(E,F)
    EF.put_mark(0.2,90,"\( {}\)".format(F.x-E.x),automatic_place=(pspict,"S"))

    AB.parameters.color="brown"
    BC.parameters.color="brown"
    CD.parameters.color="brown"
    DE.parameters.color="brown"
    EF.parameters.color="brown"

    pspict.DrawGraphs(A,B,C,D,E,F,AB,BC,CD,DE,EF)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
