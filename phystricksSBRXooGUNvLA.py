# -*- coding: utf8 -*-
from phystricks import *
def SBRXooGUNvLA():
    pspict,fig = SinglePicture("SBRXooGUNvLA")
    pspict.dilatation(0.63)

    S=Point(0,0)
    U=S+(8,0)
    F=Circle(S,3).get_point(-120)
    R=F+U-S
    J=F+(5.5,0)
    K=J+U-R

    parall=Polygon(S,U,R,F)
    parall.put_mark(0.2,points_names="SURF",pspict=pspict)
    J.put_mark(0.2,angle=-90,text="\( J\)",pspict=pspict)

    s1=Segment(S,J)
    s2=Segment(J,U)
    s3=Segment(J,K)

    no_symbol(parall.vertices,J)

    pspict.DrawGraphs(parall,s1,s2,s3,J)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
