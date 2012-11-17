# -*- coding: utf8 -*-
from phystricks import *
def SurfacesCubesclGZD():
    pspicts,fig = MultiplePictures("SurfacesCubesclGZD",6)
    pspicts[0].mother.caption=""
    pspicts[1].mother.caption=""
    pspicts[2].mother.caption="Quelle est la mesure de l'angle en \( A\) ?"
    pspicts[3].mother.caption=""
    pspicts[4].mother.caption="Les points \( I\) et \( J\) sont les milieux de \( (DH)\) et \( (CG)\)."
    pspicts[5].mother.caption=""

    for psp in pspicts:
        psp.dilatation(0.8)
        #psp.dilatation_Y(1)
        #psp.dilatation_X(1)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspicts[0])

    surface1=Polygon(cube.E,cube.F,cube.C,cube.D)
    surface1.parameters.filled()
    surface1.parameters.fill.color="brown"

    surface2=Polygon(cube.A,cube.H,cube.E)
    surface2.parameters.filled()
    surface2.parameters.fill.color="red"

    surface3=Polygon(cube.A,cube.H,cube.F)
    surface3.parameters.filled()
    surface3.parameters.fill.color="green"

    surface4=Polygon(cube.A,cube.F,cube.D)
    surface4.parameters.filled()
    surface4.parameters.fill.color="yellow"

    I=Segment(cube.D,cube.H).center()
    J=Segment(cube.C,cube.G).center()
    I.put_mark(0.3,180,"\( I\)",automatic_place=pspicts[0])
    J.put_mark(0.3,0,"\( J\)",automatic_place=pspicts[0])

    surface5=Polygon(I,J,cube.B,cube.A)
    surface5.parameters.filled()
    surface5.parameters.fill.color="cyan"

    surface6=Polygon(cube.E,cube.B,cube.C,cube.H)
    surface6.parameters.filled()
    surface6.parameters.fill.color="lightgray"

    pspicts[0].DrawGraphs(surface1,cube)
    pspicts[1].DrawGraphs(surface2,cube)
    pspicts[2].DrawGraphs(surface3,cube)
    pspicts[3].DrawGraphs(surface4,cube)
    pspicts[4].DrawGraphs(surface5,I,J,cube)
    pspicts[5].DrawGraphs(surface6,cube)

    fig.conclude()
    fig.write_the_file()
