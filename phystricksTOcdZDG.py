# -*- coding: utf8 -*-
from phystricks import *

def plasma(s):
    t=Segment(s.I,s.F)
    t.wave(0.2,0.1)
    t.parameters.color="blue"
    s.parameters.color="red"
    return s,t

def TOcdZDG():
    pspict,fig = SinglePicture("TOcdZDG")
    pspict.dilatation(1)

    A=Point(1,0)
    B=Point(5,0)
    v1=Vector(1,1)
    v2=Vector(-1,3)
    tir1=Segment(A,vector=v1).dilatationF(2)
    tir2=Segment(B,vector=v2)

    pspict.DrawGraphs(plasma(tir1),plasma(tir2))
    pspict.DrawDefaultGrid()
    fig.conclude()
    fig.write_the_file()
