# -*- coding: utf8 -*-
from phystricks import *
def QDPKooICzieh():
    pspict,fig = SinglePicture("QDPKooICzieh")
    pspict.dilatation(1)

    A=Point(0,0)
    O=Point(2,1)
    angle=Segment(A,O).angle().degree
    cer=Circle(O,(A-O).length()).graph(angle-30,angle+30)
    cer.parameters.style="dashed"
    ddroite=Segment(A,O+2*AffineVector(A,O))
    ddroite.parameters.style="dashed"
    Ap=Intersection(cer,ddroite)[1]
    seg=Segment(A,Ap)
    seg.divide_in_two(n=2,d=0.1,l=0.3,angle=45+angle,pspict=pspict)

    A.put_mark(0.2,90+45+angle,"\( A\)",automatic_place=(pspict,"corner"))
    O.put_mark(0.2,-90+angle,"\( O\)",automatic_place=(pspict,"corner"))
    Ap.put_mark(0.2,45+angle,"\( A'\)",automatic_place=(pspict,"corner"))

    pspict.DrawGraphs(A,O,Ap,cer,ddroite,seg)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
