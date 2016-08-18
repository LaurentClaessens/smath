# -*- coding: utf8 -*-
from phystricks import *
def GJMFooFKVCyK():
    pspict,fig = SinglePicture("GJMFooFKVCyK")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    l=3
    perspective=ObliqueProjection(30,0.5)
    cube=perspective.cuboid((0,0),3,1,2)
    #cube.put_vertex_mark(pspict)

    measureAE=MeasureLength(Segment(cube.A,cube.E),-0.1)
    measureAE.put_mark(0.2,angle=None,added_angle=0,text="\( 2\)",pspict=pspict)

    measureEF=MeasureLength(Segment(cube.E,cube.F),-0.1)
    measureEF.put_mark(0.2,angle=None,added_angle=0,text="\( 3\)",pspict=pspict)

    measureAD=MeasureLength(Segment(cube.A,cube.D),0.1)
    measureAD.put_mark(0.2,angle=None,added_angle=0,text="\( 1\)",pspict=pspict)

    pspict.DrawGraphs(cube,measureAE,measureEF,measureAD)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
