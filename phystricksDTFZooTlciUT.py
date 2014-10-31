# -*- coding: utf8 -*-
from phystricks import *
def DTFZooTlciUT():
    pspict,fig = SinglePicture("DTFZooTlciUT")
    pspict.dilatation(0.7)

    O=Point(0,0)
    cer=Circle(O,sqrt(18))
    
    T=cer.get_point(90+45)
    P=cer.get_point(45)
    L=cer.get_point(-70)

    T.put_mark(0.2,90+45,"Tristan",automatic_place=(pspict,"corner"))
    P.put_mark(0.2,45,"Perceval",automatic_place=(pspict,"corner"))
    L.put_mark(0.2,-70,"Lancelot",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(T,P,L)
    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

