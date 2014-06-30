# -*- coding: utf8 -*-

from phystricks import *
def ExoGraphIneqPgErDr():
    pspicts,fig = MultiplePictures("ExoGraphIneqPgErDr",4)
    pspicts[0].mother.caption=u"Résoudre \( f(x)>0\)"
    pspicts[1].mother.caption=u"Résoudre \( f(x)\leq 0\)"
    pspicts[2].mother.caption=u"Résoudre \( f(x)\geq 2\)"
    pspicts[3].mother.caption=u"Résoudre \( f(x)<-1\)"


    for psp in pspicts:
        psp.dilatation_Y(0.7)
        psp.dilatation_X(0.7)

    x=var('x')
    f=[]
    f.append( LagrangePolynomial([Point(-1,0),Point(2,0),Point(0,3)]).graph(-2,2.5)  )
    f.append( phyFunction((x-1)**2+1).graph(-1,3) )
    f.append( LagrangePolynomial( [  Point(-3,2),Point(-0.5,2),Point(1,2),Point(2.5,2),Point(1.5,3),Point(3,-2),Point(-2,4),Point(-4,0) ] ).graph(-4,3) )
    f.append( LagrangePolynomial([Point(-4,1),Point(-2.5,-1),Point(-2,-2.5),Point(-1,-1),Point(0,2),Point(1,2.5),Point(2.5,-1),Point(3,-2),Point(3.5,-1.5)]).graph(-3.5,3.5) )


    for i,psp in enumerate(pspicts):
        psp.DrawGraphs(f[i])
        psp.DrawDefaultAxes()
        psp.DrawDefaultGrid()

    fig.conclude()
    fig.write_the_file()
