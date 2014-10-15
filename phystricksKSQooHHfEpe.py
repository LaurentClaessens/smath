# -*- coding: utf8 -*-
from phystricks import *
def KSQooHHfEpe():
    pspict,fig = SinglePicture("KSQooHHfEpe")
    pspict.dilatation(1)

    A=Point(0,1)
    B=Point(4,1)

    AB=Segment(A,B)
    med=AB.bisector()

    A.put_mark(0.2,180+45,"\( A\)",automatic_place=(pspict,"corner"))
    B.put_mark(0.2,-45,"\( B\)",automatic_place=(pspict,"corner"))

    rh1=RightAngle(AB,med,0.2,0,1)
    rh2=RightAngle(AB,med,0.2,1,1)
    #rh1.parameters.color="red"
    #rh2.parameters.color="blue"

    O=AB.center()

    AO=Segment(A,O)
    OB=Segment(O,B)
    AO.put_mark(0,0,"//",automatic_place=(pspict,"center"))
    OB.put_mark(0,0,"//",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(AB,med,A,B,rh1,rh2,AO,OB)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
