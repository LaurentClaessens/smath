# -*- coding: utf8 -*-
from phystricks import *
def OGWJooWdCsvT():
    pspict,fig = SinglePicture("OGWJooWdCsvT")
    pspict.dilatation(1)

    r=3
    alpha=30
    beta=180-2*alpha
    A=Point(0,0)
    B=Circle(A,r).get_point(alpha)
    C=Circle(A,r).get_point(180-alpha)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspict=pspict)

    angA=Angle(B,A,C,r=0.3)
    angB=Angle(C,B,A,r=0.6)
    angC=Angle(A,C,B,r=0.6)

    for P in trig.vertices:
        P.parameters.symbol=''

    angA.put_mark(0.2,None,"\("+str(beta)+" \)",automatic_place=(pspict,"center"))
    angB.put_mark(0.2,None,"\("+str(alpha)+" \)",automatic_place=(pspict,"center"))
    angC.put_mark(0.2,None,"\("+str(alpha)+" \)",automatic_place=(pspict,"center"))

    pspict.DrawGraphs(trig,angA,angB,angC)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
