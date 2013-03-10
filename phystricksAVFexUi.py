# -*- coding: utf8 -*-
from phystricks import *
def AVFexUi():
    pspicts,fig = MultiplePictures("AVFexUi",2)
    pspicts[0].mother.caption=u"Les points intéressants sur les ordonnées et sur la courbe."
    pspicts[1].mother.caption=u"Les points intéressants sur l'hyperbole et sur les abscisses."

    for psp in pspicts:
        psp.dilatation_X(0.3)
        psp.dilatation_Y(2.5)

    x=var('x')
    mx=-10
    Mx=-mx
    f=phyFunction(1/x).graph(mx,Mx)
    f.cut_y(-1.2,1.2)

    a=0.7
    b=-0.3
    B1=Point(0,b)
    B2=Point(0,a)
    x1=f.inverse(b)[0]
    x2=f.inverse(a)[0]
    X1=Point(x1,0)
    X2=Point(x2,0)
    A1=f.get_point(x1)
    A2=f.get_point(x2)
    l1=Segment(X1,A1)
    l2=Segment(A1,B1)
    l3=Segment(X2,A2)
    l4=Segment(B2,A2)
    for s in [l1,l2,l3,l4]:
        s.parameters.color="red"
        s.parameters.style="dashed"

    B1.put_mark(0.2,0,"\( -1/10\)",automatic_place=(pspicts[0],"W"))
    X1.put_mark(0.2,90,"\( -10\)",automatic_place=(pspicts[0],"S"))
    B2.put_mark(0.2,180,"\( 3/4\)",automatic_place=pspicts[0])
    X2.put_mark(0.2,-90,"\( 4/3\)",automatic_place=pspicts[0])

    w1=Segment( B1,B2  )
    w1.parameters.color="cyan"
    w1.wave(0.05,0.5)

    w2=f.graph(mx,x1)
    w3=f.graph(x2,Mx)
    for w in [w2,w3]:
        w.parameters.color="red"
        w.wave(0.4,0.05)

    ws1=Segment(Point(mx,0),Point(x1,0))
    ws2=Segment(Point(x2,0),Point(Mx,0))
    for w in [ws1,ws2]:
        w.parameters.color="green"
        w.wave(0.4,0.05)

    for psp in pspicts:
        psp.DrawGraphs(f)

    pspicts[0].DrawGraphs(w1,w2,w3,l1,l2,l3,l4,A1,A2,B1,B2,X1,X2)
    pspicts[1].DrawGraphs(w2,w3,X1,X2,ws1,ws2)

    for psp in pspicts:
        psp.axes.no_graduation()
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()



