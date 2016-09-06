# -*- coding: utf8 -*-
from phystricks import *
def YDAooMNHhCN():
    pspicts,figs = IndependentPictures("YDAooMNHhCN",4)

    for psp in pspicts:
        psp.dilatation(1.5)

    a=2
    b=1
    l=a+b

    tA=Point(0,0)
    tB=Point(a,0)
    tC=Point(0,b)
    gen_trig=Polygon(tA,tB,tC)
    gen_c=[  s.midpoint() for s in gen_trig.edges  ]
    for c in gen_c:
        c.parameters.symbol=""
    gen_c[0].put_mark(0.2,-90,"\( b\)",pspict=pspicts,position="N")
    gen_c[1].put_mark(0.2,45,"\( c\)",pspict=pspicts,position="corner")
    gen_c[2].put_mark(0.2,180,"\( a\)",pspict=pspicts,position="E")
    gen_rh=RightAngle( gen_trig.edges[0],gen_trig.edges[2],1,0  )
    
    gen_alpha=AngleAOB(tC,tB,tA)
    gen_alpha.put_mark(0.2,None,"\( \\alpha\)",pspict=pspicts)
    gen_beta=AngleAOB( tA,tC,tB)
    gen_beta.put_mark(0.2,None,"\( \\beta\)",pspict=pspicts)
    pspicts[2].DrawGraphs(gen_c,gen_trig,gen_rh,gen_alpha,gen_beta)


    A=Point(0,0)
    B=A+(l,0)
    C=B-(0,l)
    D=C-(l,0)

    grand=Polygon(A,B,C,D)

    M=A+(b,0)
    N=B-(0,b)
    O=D+(a,0)
    P=D+(0,b)

    carre=Polygon(M,N,O,P)
    carre.parameters.filled()
    carre.parameters.fill.color="lightgray"

    A.put_mark(0.2,90+45,"\( A\)",pspict=pspicts,position="corner")
    B.put_mark(0.2,45,"\( B\)",pspict=pspicts,position="corner")
    C.put_mark(0.2,-45,"\( C\)",pspict=pspicts,position="corner")
    D.put_mark(0.2,180+45,"\( D\)",pspict=pspicts,position="corner")
    M.put_mark(0.2,90,"\( M\)",pspict=pspicts,position="S")
    N.put_mark(0.2,0,"\( N\)",pspict=pspicts,position="W")
    O.put_mark(0.2,-90,"\( O\)",pspict=pspicts,position="N")
    P.put_mark(0.2,180,"\( P\)",pspict=pspicts,position="E")

    a1=AngleAOB(M,P,A)
    a2=AngleAOB(N,M,B)
    b1=AngleAOB(A,M,P)
    b2=AngleAOB(B,N,M)

    a1.put_mark(0.2,None,"\( \\alpha\)",pspict=pspicts)
    a2.put_mark(0.2,None,"\( \\alpha\)",pspict=pspicts)
    b1.put_mark(0.2,None,"\( \\beta\)",pspict=pspicts)
    b2.put_mark(0.2,None,"\( \\beta\)",pspict=pspicts)

    cen=[]
    cen.append(Segment( A,M  ).center())
    cen[-1].put_mark(0.2,90,"\( a\)",pspict=pspicts,position="S")
    cen.append(Segment( M,B  ).center())
    cen[-1].put_mark(0.2,90,"\( b\)",pspict=pspicts,position="S")
    cen.append(Segment( B,N  ).center())
    cen[-1].put_mark(0.2,0,"\( a\)",pspict=pspicts,position="W")
    cen.append(Segment( N,C  ).center())
    cen[-1].put_mark(0.2,0,"\( b\)",pspict=pspicts,position="W")
    cen.append(Segment( C,O  ).center())
    cen[-1].put_mark(0.2,-90,"\( a\)",pspict=pspicts,position="N")
    cen.append(Segment( D,O  ).center())
    cen[-1].put_mark(0.2,-90,"\( b\)",pspict=pspicts,position="N")
    cen.append(Segment( D,P  ).center())
    cen[-1].put_mark(0.2,180,"\( a\)",pspict=pspicts,position="E")
    cen.append(Segment( P,A  ).center())
    cen[-1].put_mark(0.2,180,"\( b\)",pspict=pspicts,position="E")
    cen.append(Segment( M,P  ).center())
    cen[-1].put_mark(0.2,cen[-1].advised_mark_angle(pspicts),"\( c\)",pspict=pspicts,position="corner")
    for p in cen:
        p.parameters.symbol=""
    cen2=[ cen[2],cen[3],cen[4],cen[5],cen[6] ]

    K=Point( O.x,P.y )
    L=Point(O.x,N.y)
    R=Point(O.x,B.y)

    com1=Segment(R,O)
    com2=Segment(L,N)
    com3=Segment(P,K)
    com4=Segment(P,O)
    com5=Segment(O,N)

    R.put_mark(0.2,90,"\( R\)",pspict=pspicts,position="S")
    L.put_mark(0.2,180,"\( L\)",pspict=pspicts,position="E")
    K.put_mark(0.2,90+45,"\( K\)",pspict=pspicts,position="corner")

    for pspict in [  pspicts[0],pspicts[1],pspicts[3] ] :
        pspict.DrawGraphs(grand,A,B,C,D,O,P)
    pspicts[0].DrawGraphs(M,N)
    pspicts[0].DrawGraphs(carre,a1,a2,b1,b2,cen)

    pspicts[3].DrawGraphs(M,N)
    pspicts[3].DrawGraphs(carre)

    car_moyen=Polygon(A,R,K,P)
    car_petit=Polygon(R,B,N,L)
    car_petit.parameters.filled()
    car_petit.parameters.fill.color="lightgray"
    car_moyen.parameters.filled()
    car_moyen.parameters.fill.color="lightgray"
    pspicts[1].DrawGraphs(car_petit,car_moyen,N,com1,com2,com3,com4,com5,R,K,L,cen2)

    for fig in figs:
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
