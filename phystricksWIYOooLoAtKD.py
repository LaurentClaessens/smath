# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def WIYOooLoAtKD():
    pspict,fig = SinglePicture("WIYOooLoAtKD")

    cone_radius=4

    perspective=ObliqueProjection(20,0.4)
    cone_height=5
    cone_circle=Circle3D(perspective, (0,0,0),(cone_radius,0,0),(0,0,cone_radius) )
    cone_circle.linear_plotpoints=30
    cone_circle.divide=True
    alpha=pi+pi/3
    P=perspective.point(cone_radius*cos(alpha),0,cone_radius*sin(alpha))

    recone_circle=Circle3D(perspective, (0,cone_height/2,0),(cone_radius/2,cone_height/2,0),(0,cone_height/2,cone_radius/2) )
    recone_circle.linear_plotpoints=30
    recone_circle.divide=True

    S=perspective.point(0,cone_height,0)
    I=perspective.point(0,0,0)
    K=cone_circle.xmin()
    L=cone_circle.xmax()
    SK=Segment(S,K)
    SL=Segment(S,L)

    A=Point(0,0)
    B=Point(cone_radius,0)
    C=Point(0,cone_height)

    S.put_mark(0.2,angle=45,text="\( S\)",automatic_place=(pspict,""))
    I.put_mark(0.2,angle=24,text="\( I\)",automatic_place=(pspict,""))
    #P.put_mark(0.2,angle=None,text="\( P\)",automatic_place=(pspict,""))

    hauteur=Segment(I,S)
    hauteur.parameters.style='dashed'
    rayon=Segment(I,P)

    rayon.put_mark(0.2,angle=None,added_angle=180,text="\( 3\)",automatic_place=(pspict,""))
    hauteur.put_mark(0.2,angle=None,text="\( 7\)",automatic_place=(pspict,""))

    no_symbol(S)

    pspict.DrawGraphs(cone_circle,SK,SL,I,S,hauteur,P,rayon,recone_circle)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

