# -*- coding: utf8 -*-
from phystricks import *
def LOBVHYF():
    pspict,fig = SinglePicture("LOBVHYF")
    pspict.dilatation(3)

    my=1.7
    R=1
    O=Point(0,0)
    Cer=Circle(O,R)
    ligne=AffineVector( Point(R,-my),Point(R,my) )
    ligne.parameters.color="red"

    OX=Segment(Point(-1.3,0),Point(1.3,0))
    OY=Segment(Point(0,-1.3),Point(0,1.3))

    alpha=50
    M=Cer.get_point(alpha)
    M.put_mark(0.2,90,"\( M\)",pspict=pspict,position="S")
    X=Point(R,radian(alpha))
    X.put_mark(0.2,0,"\( x\)",pspict=pspict)


    s=AffineVector(X,M)
    s.parameters.color="blue"
    s.parameters.style="dashed"

    lv=Segment(Point(1,0),Point(1,X.y))
    lv.parameters.color="green"
    Cv=Cer.graph(0,alpha)
    Cv.parameters.color="green"

    C=M.projection(pspict.axes.single_axeX)
    S=M.projection(pspict.axes.single_axeY)

    C.put_mark(0.2,-90,"\( \cos(x)\)",pspict=pspict,position="N")
    S.put_mark(0.2,180,"\( \sin(x)\)",pspict=pspict,position="E")

    MC=Segment(M,C)
    MS=Segment(M,S)

    MC.parameters.color="blue"
    MC.parameters.style="dotted"
    MS.parameters.color="blue"
    MS.parameters.style="dotted"

    pspict.DrawGraphs(ligne,Cer,M,X,s,OX,OY,MC,MS,C,S,lv,Cv)
    pspict.DrawDefaultAxes()

    pspict.axes.no_graduation()

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
