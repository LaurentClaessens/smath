# -*- coding: utf8 -*-
from phystricks import *
def ZSAooVHmHWd():
    pspict,fig = SinglePicture("ZSAooVHmHWd")

    pspict.dilatation(0.6)

    O=Point(0,0)
    circonscrit=Circle(  O,3  )

    A=circonscrit.get_point(0*degree)
    B=circonscrit.get_point(80*degree)
    C=circonscrit.get_point((180+20)*degree)

    trig=Polygon(A,B,C)

    mediatrices=[]
    for seg in trig.edges:
        media=seg.bisector()
        mediatrices.append(media)

    mediatrices[0]=mediatrices[0].add_size(1.7,0)
    mediatrices[1]=mediatrices[1].add_size(2,0)
    mediatrices[2]=mediatrices[2].add_size(0,1)

    for med in mediatrices :
        med.parameters.style="dashed"

    A.put_mark(0.2,A.advised_mark_angle(pspict),"\( A\)",pspict=pspict)
    B.put_mark(0.2,B.advised_mark_angle(pspict),"\( B\)",pspict=pspict)
    C.put_mark(0.2,C.advised_mark_angle(pspict),"\( C\)",pspict=pspict)
    O.put_mark(0.4,0,"\( O\)",pspict=pspict,position="W")

    pspict.DrawGraphs(trig,mediatrices,circonscrit,A,B,C,O)

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
