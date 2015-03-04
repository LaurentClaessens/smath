# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
def CylindresxKDOdy():
    pspicts,fig = MultiplePictures("CylindresxKDOdy",2)
    pspicts[0].mother.caption=u"Un cylindre"
    pspicts[1].mother.caption=u"Un cône"

    for psp in pspicts:
        psp.dilatation(0.6)
        #psp.dilatation_Y(1)
        #psp.dilatation_X(1)

    c=5
    h=3

    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),c,h,c)
    Ch=Circle3D(perspective,(c/2,h,c/2),(c,h,c/2),(c/2,h,c))

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
    surfV.parameters.fill.color="brown"

    measureH=MeasureLength(cube.segc1[2],-0.2)
    measureH.put_mark(0.2,None,"\SI{5}{\centi\meter}",automatic_place=pspicts[0])
    measureP=MeasureLength(cube.segP[2],0.2)
    measureP.put_mark(0.2,None,"\SI{5}{\centi\meter}",automatic_place=pspicts[0])
    measureV=MeasureLength(cube.segc1[3],-0.2)
    measureV.put_mark(0.2,None,"\SI{3}{\centi\meter}",automatic_place=(pspicts[1],"E"))

    S=perspective.point(c/2,0,c/2)
    Iph=min(  Ch.graph(-pi/4,pi/4).curve2d.points_list,key=lambda P: P.y/abs(P.x-S.x)   )
    Jph=min(  Ch.graph(3*pi/4,5*pi/4).curve2d.points_list,key=lambda P: P.y/abs(P.x-S.x)   )
    diag1=Segment(S,Iph)
    diag2=Segment(Jph,S)
    surf_cone=CustomSurface(diag1,Ch.graph(pi,2*pi).curve2d,diag2)
    surf_cone.parameters.filled()
    surf_cone.parameters.fill.color="brown"

    d1=Segment(cube.c2[3],cube.c1[2])
    d2=Segment(cube.c2[2],cube.c1[3])
    d1.parameters.style="dotted"
    d1.parameters.color="red"
    d2.parameters.style="dotted"
    d2.parameters.color="red"

    pspicts[0].DrawGraphs(measureH,measureP,measureV,surfV,surfb,surfh,Ch,Cb1,Cb2,cube)
    pspicts[1].DrawGraphs(diag2,surfh,surf_cone,diag1,Ch,cube,diag2)


    fig.conclude()
    fig.write_the_file()

