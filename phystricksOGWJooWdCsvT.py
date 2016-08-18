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
    angC=AngleAOB(A,C,B)

    trig=Polygon(A,B,C)
    trig.put_mark(0.2,pspict=pspict)

    angA=AngleAOB(B,A,C)
    angB=AngleAOB(C,B,A)

    for P in trig.vertices:
        P.parameters.symbol=''

    angA.put_mark(0.2,None,"\("+str(beta)+" \)",pspict=pspict,position="center")
    angB.put_mark(0.2,None,"\("+str(alpha)+" \)",pspict=pspict,position="center")
    angC.put_mark(0.2,None,"\("+str(alpha)+" \)",pspict=pspict,position="center")

    pspict.DrawGraphs(trig,angA,angB,angC)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
