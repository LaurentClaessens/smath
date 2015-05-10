# -*- coding: utf8 -*-
from phystricks import *
def LWKNooOqJykO():
    pspict,fig = SinglePicture("LWKNooOqJykO")
    pspict.dilatation_X(1)
    pspict.dilatation_Y(1)

    D=Point(0,0)
    F=D+(8,0)
    I=Segment(D,F).midpoint()
    cerI=CircleOA(I,D)
    cerD=Circle(D,3)
    E=Intersection(cerI,cerD)[0]

    I.put_mark(0.2,angle=None,added_angle=0,text="\( I\)",automatic_place=(pspict,""))

    EI=Segment(E,I)    # Rien que cela justifie le nom des points ahahaha

    trig=Polygon(D,E,F)
    trig.put_mark(0.2,points_names="DEF",pspict=pspict)


    trig.edges[2].divide_in_two(n=2,d=0.1,l=0.3,angle=45,pspict=pspict)

    no_symbol(trig.vertices)
    pspict.DrawGraphs(trig,I,EI)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
