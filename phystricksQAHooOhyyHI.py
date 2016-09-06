# -*- coding: utf8 -*-
from phystricks import *
def QAHooOhyyHI():
    pspicts,figs = IndependentPictures("QAHooOhyyHI",3)

    for psp in pspicts:
        psp.dilatation(0.7)

    F=Point(0,0)
    G=Point(6,0)
    S=Circle(G,9).get_point((90+45)*degree)
    H=Circle(G,7).get_point((90+45)*degree)

    triangle=Polygon(F,G,H)
    seg=Segment(G,S)
    seg.parameters.style='dashed'

    FG=triangle.edges[0]
    FG.put_measure(0.2,0.2,-90,"\( 6\)",pspict=pspicts,position="corner")
    GH=triangle.edges[1]
    GH.put_measure(0.2,0.2,45,"\( 7\)",pspict=pspicts,position="corner")


    F.put_mark(0.2,180+45,"\( F\)",pspict=pspicts,position="corner")
    G.put_mark(0.2,-45,"\( G\)",pspict=pspicts,position="corner")
    H.put_mark(0.2,45,"\( H\)",pspict=pspicts,position="corner")

    qcangle=AngleAOB(H,G,F)
    a1=AngleAOB(G,F,H)
    a2=AngleAOB(F,H,G)
    qcangle.put_mark(0.2,None,"\( 45\)",pspict=pspicts)
    a1.put_mark(0.1,None,"\( 78\)",pspict=pspicts)
    a2.put_mark(0.1,None,"\( 57\)",pspict=pspicts)
    
    pspicts[0].DrawGraphs(F,G,FG,seg,qcangle)
    pspicts[1].DrawGraphs(F,G,H,seg,triangle,qcangle)
    pspicts[2].DrawGraphs(F,G,H,triangle,qcangle,a1,a2)

    for fig in figs :
        fig.no_figure()
        fig.conclude()
        fig.write_the_file()
