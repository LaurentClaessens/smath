# -*- coding: utf8 -*-

from __future__ import division
from phystricks import *

def CYLGooSGnRii():
    pspict,fig = SinglePicture("CYLGooSGnRii")
    pspict.dilatation(0.5)

    cone_height=7
    cylinder_radius=2
    cone_radius=3
    left_height=(cone_height*cylinder_radius)/cone_radius   # WW Thalès !           this is the height left for the flower.
    cylinder_height=cone_height-left_height

    perspective=ObliqueProjection(30,0.5)
    base_circle=Circle3D(perspective, (0,0,0),(cylinder_radius,0,0),(0,0,cylinder_radius) )
    up_circle=Circle3D(perspective, (0,cylinder_height,0),(cylinder_radius,cylinder_height,0),(0,cylinder_height,cylinder_radius) )
    cone_circle=Circle3D(perspective, (0,0,0),(cone_radius,0,0),(0,0,cone_radius) )
    base_circle.parameters.style="dashed"
    cone_circle.divide=True
    up_circle.divide=True

    S=perspective.point(0,cone_height,0)
    K=cone_circle.xmin()
    L=cone_circle.xmax()
    SK=Segment(S,K)
    SL=Segment(S,L)

    S=base_circle.xmin()
    T=base_circle.xmax()
    U=up_circle.xmin()
    V=up_circle.xmax()
    h1=Segment(U,S)
    h2=Segment(V,T)

    A=Point(0,0)
    B=Point(cone_radius,0)
    C=Point(0,cone_height)
    D=Point(0,cylinder_height)
    E=Point(cylinder_radius,cylinder_height)

    F=perspective.point(0,cylinder_height,0)
    photo_size=(2*left_height/3.5)*pspict.yunit       # La photo de la fleur fera les trois demi de la partie restante
    F.put_mark(0.01,angle=90,text="\includegraphics[height="+str(photo_size)+"cm]{fp081206-28.pdf}",automatic_place=(pspict,""))
    

    pspict.comment=r"""
    \begin{enumerate}
    \item
    The dashed part is not correct because of 'GraphOfACircle3D.specific\_action\_on\_pspict' which is not precise enough when 'divide' is 'True'
    \item
    The flower is more or less on the cross in the middle of the upper circle of the cylinder.
    \item
        Are there enough plotpoints ?
    \end{enumerate}
    """
    pspict.DrawGraphs(base_circle,up_circle,cone_circle,SK,SL,h1,h2,F)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
