# -*- coding: utf8 -*-
from __future__ import division
from phystricks import *
from simul_Bernoulli import plein_de_simulations
def SimulBinNWxfTN():
    schema=[10,100,10000]
    pspicts,fig = MultiplePictures("SimulBinNWxfTN",len(schema))

    for psp in pspicts:
        psp.My_acceptable_BB=1000
        psp.Mx_acceptable_BB=1000

    for i in range(0,len(schema)):
        pspicts[i].mother.caption=u"Nous répétons "+str(schema[i])+u" expériences de \( 100\) lancers"

    for psp in pspicts:
        psp.dilatation_X(0.05)
        psp.axes.do_mx_enlarge=False
        psp.axes.do_my_enlarge=False

    for i,s in enumerate(schema):
        print s
        resultats=plein_de_simulations(nombre=s,montrer=False)
        fact=5/max(resultats.values())      # Le numérateur ici sera la hauteur du graphique
        pspicts[i].dilatation_Y(fact)
        psp.axes.single_axeY.Dx=max(resultats.values())/5
        for k in range(0,100):
            seg=Segment(Point(k,0),Point(k,resultats[k]))
            pspicts[i].DrawGraphs(seg)

    for psp in pspicts:
        psp.axes.single_axeX.Dx=10
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

