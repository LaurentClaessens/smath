# -*- coding: utf8 -*-
from phystricks import *
def KJWQooEicWkQ():
    pspict,fig = SinglePicture("KJWQooEicWkQ")
    pspict.dilatation(0.5)

    
    A=Point(0,0)
    B=A+(3,0)
    C=B+(0,-4)
    D=C+(4.5,0)
    E=D+(0,2)
    F=E+(3,0)
    G=F+(0,-6)
    H=Point(A.x,G.y)

    champ=Polygon(A,B,C,D,E,F,G,H)
    champ.put_mark(0.3,pspict=pspict)
    champ.edges[0].put_code(n=2,d=0.1,l=0.4,pspict=pspict)
    champ.edges[1].put_code(n=2,d=0.1,l=0.4,pspict=pspict)

    champ.edges[0].put_mark(0.2,angle=None,added_angle=0,text="\SI{3}{\meter}",automatic_place=(pspict,""))
    champ.edges[5].put_mark(0.2,angle=None,added_angle=0,text="\SI{9}{\meter}",automatic_place=(pspict,""))
    champ.edges[6].put_mark(0.2,angle=None,added_angle=0,text="\SI{12.5}{\meter}",automatic_place=(pspict,""))
    champ.edges[7].put_mark(0.2,angle=None,added_angle=0,text="\SI{10.5}{\meter}",automatic_place=(pspict,""))

    rhs=[  RightAngleAOB(H,A,B),RightAngleAOB(A,B,C),RightAngleAOB(B,C,D),RightAngleAOB(C,D,E),RightAngleAOB(D,E,F),RightAngleAOB(E,F,G),RightAngleAOB(F,G,H),RightAngleAOB(G,H,A)  ]
    no_symbol(champ.vertices)

    pspict.DrawGraphs(champ,rhs)
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
