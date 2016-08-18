# -*- coding: utf8 -*-
from phystricks import *

xmin=-0.5
xmax=10
ymin=-3
ymax=3
alpha=30
theta=radian(alpha)

def segin(P,theta):
    Q=Point(P.x+cos(theta),P.y+sin(theta))
    s=Segment(P,Q).inside_bounding_box(xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax)
    return s

def JHrkjFz():
    pspict,fig = SinglePicture("JHrkjFz")
    pspict.dilatation(1)

    D=Point(0,0)
    D.put_mark(0.2,90,"\( D\)",pspict=pspict)
    for i in range(-8,4):
        P=Point(0,i)
        s=segin(P,theta)
        Q=Point(0,-i)
        t=segin(Q,-theta)
        pspict.DrawGraphs(t,s)

    E=D+(  4*cos(theta),2*sin(theta)  )
    E.put_mark(0.2,90,"\( E\)",pspict=pspict)
    Ep=D+(  4*cos(theta),-2*sin(theta)  )
    Ep.put_mark(0.2,90,"\( E'\)",pspict=pspict)
    F=D+(  9*cos(theta),-3*sin(theta)  )
    F.put_mark(0.2,90,"\( F\)",pspict=pspict)

    #pspict.DrawDefaultAxes()
    pspict.DrawGraphs(D,E,Ep,F)
    fig.conclude()
    fig.write_the_file()
