# -*- coding: utf8 -*-
from phystricks import *
def RouletteACaVAA():
    pspict,fig = SinglePicture("RouletteACaVAA")
    pspict.dilatation(1)

    O=Point(0,0)
    r=2
    alpha=15
    Cer=Circle(O,r)
    A=Cer.get_point(alpha)
    B=Cer.get_point(alpha+90)

    OA=Segment(O,A)
    AO=Segment(A,O)
    OB=Segment(O,B)

    CerB=Cer.graph(alpha,alpha+90)
    ZB=CustomSurface(OA,CerB,OB)

    CerR=Cer.graph(alpha+90,370)
    ZR=CustomSurface(OB,CerR,AO)

    ZB.parameters.filled()
    ZB.parameters.fill.color="blue"
    ZR.parameters.filled()
    ZR.parameters.fill.color="red"

    vect=Vector(Cer.get_point(alpha+30))
    vect.parameters.color="yellow"

    pspict.DrawGraphs(ZB,ZR,Cer,OA,OB,vect)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
