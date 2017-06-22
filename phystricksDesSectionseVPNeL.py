# -*- coding: utf8 -*-
from phystricks import *
def DesSectionseVPNeL():

    pspicts,fig = MultiplePictures("DesSectionseVPNeL",2)
    pspicts[0].mother.caption="Des triangles"
    pspicts[1].mother.caption="Des sections"


    for psp in pspicts:
        psp.dilatation_Y(1)
        psp.dilatation_X(1)


    perspective=ObliqueProjection(30,0.5)
    rectangle=perspective.cuboid((0,0),4,4,4)

    surface1=Polygon(rectangle.c1[0],rectangle.c1[1],rectangle.c2[2],rectangle.c2[3])
    surface1.make_edges_independent()
    surface1.filled()
    surface1.fill_parameters.color="lightgray"
    surface1.edges[2].parameters.style="dashed"
    surface1.edges[3].parameters.style="dashed"


    surface2=Polygon(rectangle.c1[0],rectangle.c2[1],rectangle.c2[0])
    surface2.make_edges_independent()
    surface2.filled()
    surface2.fill_parameters.color="green"

    surface3=Polygon(rectangle.c1[1],rectangle.c1[3],rectangle.c2[2])
    surface3.make_edges_independent()
    surface3.filled()
    surface3.fill_parameters.color="red"

    pspicts[0].DrawGraphs(surface2,surface3,rectangle)
    pspicts[1].DrawGraphs(surface1,rectangle)

    fig.conclude()
    fig.write_the_file()
