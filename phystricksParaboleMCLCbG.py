# -*- coding: utf8 -*-

from phystricks import *
def ParaboleMCLCbG():
    pspicts,fig = MultiplePictures("ParaboleMCLCbG",2)
    pspicts[0].mother.caption=u"Une parabole tournée vers le haut."
    pspicts[1].mother.caption=u"Une parabole tournée vers le bas."

    for psp in pspicts :
        psp.dilatation(3)

    x=var('x')

    f=phyFunction(1.8*x**2-x-1).graph(-1.01,1.3)
    a=f.sage.coefficient(x,2)
    b=f.sage.coefficient(x,1)
    c=f.sage.coefficient(x,0)
    s=-b/(2*a)
    S=Point(s,f(s))
    sym=Segment(Point(s,-1.5),Point(s,1.5))
    sym.parameters.color="red"

    pspicts[0].axes.single_axeX.Dx=0.25
    pspicts[0].axes.single_axeY.Dx=0.5
    pspicts[0].DrawGraphs(f,sym,S)

    g=phyFunction(-1.8*x**2+x).graph(-0.75,1)
    a=f.sage.coefficient(x,2)
    b=f.sage.coefficient(x,1)
    c=f.sage.coefficient(x,0)
    s=-b/(2*a)
    T=Point(s,g(s))
    sym2=Segment(Point(s,-2),Point(s,0.5))
    sym2.parameters.color="red"

    pspicts[1].axes.single_axeX.Dx=0.5
    pspicts[1].axes.single_axeY.Dx=0.5
    pspicts[1].DrawGraphs(g,sym2,T)


    for psp in pspicts:
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
