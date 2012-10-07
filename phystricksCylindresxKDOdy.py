# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def CylindresxKDOdy():
    pspicts,fig = MultiplePictures("CylindresxKDOdy",2)
    pspicts[0].mother.caption="<+caption1+>"
    pspicts[1].mother.caption="<+caption2+>"

    for psp in pspicts:
        psp.dilatation_Y(1)
        psp.dilatation_X(1)

    c=5
    h=3

    perspective=ObliqueProjection(30,0.7)
    cube=perspective.cuboid((0,0),c,h,c)
    Ch=Circle3D(perspective,(c/2,h,c/2),(c,h,c/2),(c/2,h,c))
    #Ch.plotpoints=50

    Cb=Circle3D(perspective,(c/2,0,c/2),(c,0,c/2),(c/2,0,c))
    Cb.parameters.color="red"
    Cb1=Cb.graph(pi,2*pi)
    Cb2=Cb.graph(0,pi)
    Cb2.parameters.style="dashed"

    surfb=CustomSurface(Cb.curve2d,Segment(Cb.curve2d.F,Cb.curve2d.I))
    surfb.parameters.filled()
    surfb.parameters.fill.color="brown"
    surfh=CustomSurface(Ch.curve2d,Segment(Ch.curve2d.F,Ch.curve2d.I))
    surfh.parameters.filled()
    surfh.parameters.fill.color="brown"

    Ih=Segment(cube.A,cube.E).center()
    Ih=min(  Ch.curve2d.points_list,key=lambda P:P.x  )
    Jh=max(  Ch.curve2d.points_list,key=lambda P:P.x  )
    Ib=min(  Cb.curve2d.points_list,key=lambda P:P.x  )
    Jb=max(  Cb.curve2d.points_list,key=lambda P:P.x  )
    surfV=Polygon(Ih,Ib,Jb,Jh)
    surfV.parameters.filled()
    surfV.parameters.color="brown"


    pspicts[0].DrawGraphs(surfV,surfb,surfh,Ch,Cb1,Cb2,cube)
    pspicts[1].DrawGraphs(cube,Ch)


    fig.conclude()
    fig.write_the_file()

