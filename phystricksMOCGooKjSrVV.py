# -*- coding: utf8 -*-
from phystricks import *

def sierp_step(trig):
    P1=trig.edges[0].midpoint()
    P2=trig.edges[1].midpoint()
    P3=trig.edges[2].midpoint()
    trigs=[ Polygon(P1,trig.vertices[1],P2),Polygon(P2,P3,trig.vertices[2]),Polygon(P1,P3,trig.vertices[0])  ]
    for tr in trigs:
        tr.parameters.filled()
        tr.parameters.fill.color="lightgray"
    return trigs

moive_siepr={}
def Sierpinski(initial_trig,n):
    if n in moive_siepr.keys():
        return moive_siepr[n]
    else :
        if n==0:
            return [initial_trig]
        else :
            a=[]
            for trig in Sierpinski(initial_trig,n-1):
                a.extend(sierp_step(trig)) 
        moive_siepr[n]=a
        return a

def MOCGooKjSrVV():
    n=5
    pspicts,fig = MultiplePictures("MOCGooKjSrVV",n)
    for i in range(0,n):
        pspicts[i].mother.caption=u"Le triangle de Sierpinski numéro {}".format(i)

    for psp in pspicts:
        psp.dilatation_X(1)
        psp.dilatation_Y(1)
    
    l=3
    A=Point(0,0)
    B=Point(l,0)
    C=Circle(A,l).get_point(60)
    initial_trig=Polygon( A,B,C    )
    initial_trig.parameters.filled()
    initial_trig.parameters.fill.color="lightgray"
    sierp=[ Sierpinski(initial_trig,k) for k in range(0,n+1)  ]

    for i in range(0,n):
        pspicts[i].DrawGraphs(sierp[i])

    fig.conclude()
    fig.write_the_file()
