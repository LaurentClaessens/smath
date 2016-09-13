# -*- coding: utf8 -*-
from phystricks import *
def CBLooYAMumJ():
    pspictA,figA = SinglePicture("JJOooHGTOyn")
    pspictB,figB = SinglePicture("VAAooKPNvIs")
    pspictC,figC = SinglePicture("WNEooGHwkVN")
    pspictD,figD = SinglePicture("OSLooCtzTMX")
    pspictE,figE = SinglePicture("OPWooAJbLaM")

    pspicts=[pspictA,pspictB,pspictC,pspictD,pspictE]
    figs=[figA,figB,figC,figD,figE]

    for psp in pspicts :
        psp.dilatation_X(0.5)
        psp.dilatation_Y(0.5)

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
    d1.put_mark(0.2,None,"\( d_1\)",pspicts=pspicts,position="corner")
    d2.put_mark(0.2,None,"\( d_2\)",pspicts=pspicts,position="corner")

    A.put_mark(0.2,180,"\( A\)",pspicts=pspicts,position="E")
    B.put_mark(0.3,None,"\( B\)",pspicts=pspicts,position="corner")
    C.put_mark(0.2,None,"\( C\)",pspicts=pspicts,position="corner")

    angle=AngleAOB(C,A,B)
    angle.put_mark(0.2,alpha,"",pspicts=pspicts)

    Ap=Point(8,2)
    K=Circle(Ap,4).get_point(30)

    d1p=Segment(Ap,K).dilatation(2)
    d1p.mark_point=lambda :d1p.I
    d1p.put_mark(0.2,None,"\( d_1'\)",pspicts=pspicts,position="corner")

    Ap=((2*d1p.I+d1p.F)/3).numerical_approx()
    Ap.put_mark(0.2,d1p.advised_mark_angle(pspicts),"\( A'\)",pspicts=pspicts,position="corner")

    arc=Circle(Ap,l_isocele).graph(d1p.angle()-15,d1p.angle()+15)
    ray1=Segment(Ap, arc.get_point( arc.angleI+5 ) )
    ray1.parameters.style='dashed'
    m=ray1.midpoint()
    m.parameters.symbol=''
    m.put_mark(0.2,None,"\( AB\)",pspicts=pspicts,position="corner")

    Bp=Intersection(arc,d1p)[1].numerical_approx()
    Bp.put_mark(0.2,d1p.advised_mark_angle(pspicts)+45,"\( B'\)",pspicts=pspicts,position="corner")

    BC=Segment(B,C)
    BC.parameters.color='red'
    distBC=numerical_approx(BC.length)

    cercle2=Circle(Ap,l_isocele)
    cercle3=Circle(Bp,distBC)

    ray2=Segment(Bp,cercle3.get_point(50))
    ray2.parameters.color='red'

    #Cp=Intersection(cercle3,cercle2)[1]
    Cp=cercle2.get_point(d1p.angle()-alpha)
    Cp.put_mark(0.2,-90,"\( C'\)",pspicts=pspicts,position="corner")

    d2p=Segment(Ap,Cp).add_size_extremity(3)
    d2p.mark_point=lambda :d2p.F
    d2p.put_mark(0.2,None,"\( d'_2\)",pspicts=pspicts,position="corner")

    pspicts[0].DrawGraphs(d1,d2,A,angle,d1p,Ap)
    pspicts[1].DrawGraphs(d1,d2,A,cercle1,B,C,d1p,Ap)
    pspicts[2].DrawGraphs( d1,d2,A,cercle1,B,C,d1p,  Ap,arc,ray1,m,Bp)
    pspicts[3].DrawGraphs( d1,d2,A,B,C,d1p,  Ap,Bp,BC,cercle3,cercle2,ray2)
    pspicts[4].DrawGraphs( d1,d2,A,B,C,d1p,  Ap,Bp,Cp,cercle3,cercle2,d2p)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
