# -*- coding: utf8 -*-
from phystricks import *
def ParaboleResumeSzaWaG():
    pspicts,fig = MultiplePictures("ParaboleResumeSzaWaG",2)
    pspicts[0].mother.caption="Si \( \Delta=0\), la parabole ne touche l'axe des abscisses qu'en un seul point."
    pspicts[1].mother.caption="Si \( \Delta<0\), la parabole ne touche jamais l'axe des abscisses."

    for psp in pspicts:
        psp.dilatation_Y(1)
        psp.dilatation_X(1)

    f=LagrangePolynomial([Point(-3,2),Point(-1,1),Point(0,2)]).graph(-3,0)
    g=-LagrangePolynomial([Point(-1,2),Point(1,0),Point(3,2)]).graph(-1,3)

    pspicts[0].DrawGraphs(g)
    pspicts[1].DrawGraphs(f)

    for psp in pspicts:
        psp.DrawDefaultAxes()
        psp.axes.no_graduation()

    fig.conclude()
    fig.write_the_file()

