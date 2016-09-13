# -*- coding: utf8 -*-
from phystricks import *
def CubeLFZuiW():
    pspicts,fig = MultiplePictures("CubeLFZuiW",2)
    pspicts[0].mother.caption="Le cube"
    pspicts[1].mother.caption="Quelque mesures sur le cube"

    for psp in pspicts:
        psp.dilatation_Y(1)
        psp.dilatation_X(1)

    perspective=ObliqueProjection(45,0.5)

    l=3
    A=[Point(0,l),Point(l,l),Point(l,0),Point(0,0)]

    c1=[ perspective.point(P.x,P.y,0) for P in A ]
    c2=[ perspective.point(P.x,P.y,l) for P in A ]

    segP=[ Segment( c1[i],c2[i] ) for i in range(0,len(c1))  ]
    segc1=[ Segment(c1[i],c1[(i+1)%len(c1)]) for i in range(0,len(c1)) ]
    segc2=[ Segment(c2[i],c2[(i+1)%len(c2)]) for i in range(0,len(c2)) ]

    for i,s in enumerate(segc1):
        s.parameters.color="blue"
    for i,s in enumerate(segc2):
        s.parameters.color="green"

    segc2[2].parameters.style="dashed"
    segc2[3].parameters.style="dashed"
    segP[3].parameters.style="dashed"

    for psp in pspicts :
        psp.DrawGraphs(segP,segc1,segc2)


    alpha=AngleAOB(c1[2],c1[3],c2[3])
    alpha.parameters.color="red"
    alpha.put_mark(0.3,None,"\( \\alpha\)",pspict=pspicts[1])

    measureR=MeasureLength(segc1[2],-0.2)
    measureR.put_mark(0.2,None,"\( c\)",pspict=pspicts[1])
    measureP=MeasureLength(segP[2],0.2)
    measureP.put_mark(0.2,None,"\( k\\times c\)",pspict=pspicts[1])
    
    pspicts[1].DrawGraphs(alpha,measureR,measureP)

    fig.conclude()
    fig.write_the_file()
