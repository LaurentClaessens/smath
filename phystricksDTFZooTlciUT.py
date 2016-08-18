# -*- coding: utf8 -*-
from phystricks import *
def DTFZooTlciUT():
    pspict,fig = SinglePicture("DTFZooTlciUT")
    pspict.dilatation(1)

    O=Point(0,0)
    cer=Circle(O,sqrt(18))
    
    T=cer.get_point(90+45)
    P=cer.get_point(45)
    L=cer.get_point(-70)

    T.put_mark(0.2,90+45,"Tristan",pspict=pspict,position="corner")
    P.put_mark(0.2,45,"Perceval",pspict=pspict,position="corner")
    L.put_mark(0.2,-70,"Lancelot",pspict=pspict,position="corner")

    pspict.DrawGraphs(T,P,L)
    #pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

