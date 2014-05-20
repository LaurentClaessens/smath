# -*- coding: utf8 -*-
from phystricks import *
def YORfWSM():
    pspict,fig = SinglePicture("YORfWSM")
    pspict.dilatation(2)

    my=1.7
    O=Point(0,0)
    Cer=Circle(O,1)
    ligne=AffineVector( Point(1,-my),Point(1,my) )
    ligne.parameters.color="red"

    alpha=75
    M=Cer.get_point(alpha)
    M.put_mark(0.2,M.advised_mark_angle,"\( M\)",automatic_place=pspict)
    X=Point(1,radian(alpha))
    X.put_mark(0.2,0,"\( x\)",automatic_place=pspict)

    lv=Segment(Point(1,0),Point(1,X.y))
    lv.parameters.color="green"
    Cv=Cer.graph(0,alpha)
    Cv.parameters.color="green"

    s=AffineVector(X,M)
    s.parameters.color="blue"
    s.parameters.style="dashed"

    pspict.DrawGraphs(ligne,Cer,lv,Cv,M,X,s)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
