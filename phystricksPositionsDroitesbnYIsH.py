# -*- coding: utf8 -*-
from phystricks import *
def PositionsDroitesbnYIsH():
    pspicts,fig = MultiplePictures("PositionsDroitesbnYIsH",4)
    pspicts[0].mother.caption="Deux droites coplanaires qui se coupent en \( B\)"
    pspicts[1].mother.caption="Deux autres droites coplanaires."
    pspicts[2].mother.caption="Deux droites non coplanaires."
    pspicts[3].mother.caption="Deux autres droites non coplanaires."

    for psp in pspicts:
        psp.dilatation_Y(1)
        psp.dilatation_X(1)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),l,l,l)
    cube.put_vertex_mark(pspicts[0])

    dilatation=1.5
    AB=Segment(cube.A,cube.B).dilatation(dilatation)
    BC=Segment(cube.B,cube.C).dilatation(dilatation)
    AB.parameters.color="red"
    BC.parameters.color="red"
    pspicts[0].DrawGraphs(cube,AB,BC)

    EC=Segment(cube.E,cube.C).dilatation(dilatation)
    BH=Segment(cube.B,cube.H).dilatation(dilatation)
    EC.parameters.color="red"
    BH.parameters.color="red"
    pspicts[1].DrawGraphs(cube,EC,BH)

    AE=Segment(cube.A,cube.E).dilatation(dilatation)
    BG=Segment(cube.B,cube.G).dilatation(dilatation)
    AE.parameters.color="red"
    BG.parameters.color="red"
    pspicts[2].DrawGraphs(cube,AE,BG)

    HF=Segment(cube.H,cube.F).dilatation(dilatation)
    AC=Segment(cube.A,cube.C).dilatation(dilatation)
    HF.parameters.color="red"
    AC.parameters.color="red"
    pspicts[3].DrawGraphs(cube,HF,AC)

    fig.conclude()
    fig.write_the_file()
