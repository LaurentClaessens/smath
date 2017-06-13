# -*- coding: utf8 -*-
from phystricks import *

def makeCBL(pspict,num):
    pspict.dilatation_X(0.5)
    pspict.dilatation_Y(0.5)

    alphaI=-20
    alpha=70
    l_isocele=4

    A=Point(0,0)
    cercle1=Circle(A,l_isocele).graph(alphaI-10,alphaI+alpha+10)
    B=cercle1.get_point(alphaI+alpha)
    C=cercle1.get_point(alphaI)

    d1=Segment(A,B).add_size_extremity(2)
    d2=Segment(A,C).add_size_extremity(2)
    d1.mark_point=lambda :d1.F
    d2.mark_point=lambda :d2.F
    d1.put_mark(0.2,text="\( d_1\)",pspict=pspict,position="corner")
    d2.put_mark(0.2,text="\( d_2\)",pspict=pspict,position="corner")

    A.put_mark(0.2,text="\( A\)",pspict=pspict,position="E")
    B.put_mark(0.3,text="\( B\)",pspict=pspict,position="corner")
    C.put_mark(0.2,text="\( C\)",pspict=pspict,position="corner")

    angle=AngleAOB(C,A,B)

    Ap=Point(8,2)
    K=Circle(Ap,4).get_point(30)

    d1p=Segment(Ap,K).dilatation(2)
    d1p.mark_point=lambda :d1p.I
    d1p.put_mark(0.2,None,"\( d_1'\)",pspict=pspict,position="corner")

    Ap=((2*d1p.I+d1p.F)/3).numerical_approx()
    Ap.put_mark(0.2,d1p.advised_mark_angle(pspict),"\( A'\)",pspict=pspict,position="corner")

    arc=Circle(Ap,l_isocele).graph(d1p.angle().degree-15,d1p.angle().degree+15)
    ray1=Segment(Ap, arc.get_point( arc.angleI.degree+5 ) )
    ray1.parameters.style='dashed'
    m=ray1.midpoint()
    m.parameters.symbol=''
    m.put_mark(0.2,None,"\( AB\)",pspict=pspict,position="corner")

    Bp=Intersection(arc,d1p)[1].numerical_approx()
    Bp.put_mark(0.2,d1p.advised_mark_angle(pspict),added_angle=45,text="\( B'\)",pspict=pspict,position="corner")

    BC=Segment(B,C)
    BC.parameters.color='red'
    distBC=numerical_approx(BC.length)

    cercle2=Circle(Ap,l_isocele)
    cercle3=Circle(Bp,distBC)

    ray2=Segment(Bp,cercle3.get_point(50))
    ray2.parameters.color='red'

    #Cp=Intersection(cercle3,cercle2)[1]
    Cp=cercle2.get_point(d1p.angle().degree-alpha)
    Cp.put_mark(0.2,-90,"\( C'\)",pspict=pspict,position="corner")

    d2p=Segment(Ap,Cp).add_size_extremity(3)
    d2p.mark_point=lambda :d2p.F
    d2p.put_mark(0.2,None,"\( d'_2\)",pspict=pspict,position="corner")
    if num==0:
        pspict.DrawGraphs(d1,d2,A,angle,d1p,Ap)
    if num==1:
        pspict.DrawGraphs(d1,d2,A,cercle1,B,C,d1p,Ap)
    if num==2:
        pspict.DrawGraphs( d1,d2,A,cercle1,B,C,d1p,  Ap,arc,ray1,m,Bp)
    if num==3:
        pspict.DrawGraphs( d1,d2,A,B,C,d1p,  Ap,Bp,BC,cercle3,cercle2,ray2)
    if num==4:
        pspict.DrawGraphs( d1,d2,A,B,C,d1p,  Ap,Bp,Cp,cercle3,cercle2,d2p)

def JJOooHGTOyn():
    pspict,fig = SinglePicture("JJOooHGTOyn")
    makeCBL(pspict,0)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def VAAooKPNvIs():
    pspict,fig = SinglePicture("VAAooKPNvIs")
    makeCBL(pspict,1)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def WNEooGHwkVN():
    pspict,fig = SinglePicture("WNEooGHwkVN")
    makeCBL(pspict,2)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def OSLooCtzTMX():
    pspict,fig = SinglePicture("OSLooCtzTMX")
    makeCBL(pspict,3)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def OPWooAJbLaM():
    pspict,fig = SinglePicture("OPWooAJbLaM")
    makeCBL(pspict,4)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

