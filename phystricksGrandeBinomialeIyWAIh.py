# -*- coding: utf8 -*-
from phystricks import *
def GrandeBinomialeIyWAIh():
    pspicts,fig = MultiplePictures("GrandeBinomialeIyWAIh",4)
    pspicts[0].mother.caption="\( n=40\), \( p=0.25\)"
    pspicts[1].mother.caption="\( n=80\), \( p=0.25\)"
    pspicts[2].mother.caption="\( n=40\), \( p=0.85\)"
    pspicts[3].mother.caption="\( n=80\), \( p=0.85\)"

    for psp in pspicts:
        psp.dilatation_X(0.11)
        psp.dilatation_Y(35)

    from scipy import stats

    XX=[]

    XX.append(stats.binom(40,0.25))
    XX.append(stats.binom(80,0.25))
    XX.append(stats.binom(40,0.85))
    XX.append(stats.binom(80,0.85))

    for i,psp in enumerate(pspicts):
        X=XX[i]
        n=X.args[0]
        p=X.args[1]
        for k in range(0,n+1):
            y=X.pmf(k)
            seg=Segment(Point(k,0),Point(k,y))
            seg.parameters.color="blue"
            seg.parameters.add_option("linewidth","0.7mm")
            psp.DrawGraphs(seg)

    for psp in pspicts:
        psp.axes.single_axeX.Dx=10
        psp.axes.single_axeY.Dx=0.05
        psp.axes.do_mx_enlarge=False
        psp.axes.do_my_enlarge=False
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
