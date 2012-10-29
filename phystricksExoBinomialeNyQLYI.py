# -*- coding: utf8 -*-
from phystricks import *
def ExoBinomialeNyQLYI():
    pspicts,fig = MultiplePictures("ExoBinomialeNyQLYI",4)
    pspicts[0].mother.caption=""
    pspicts[1].mother.caption=""
    pspicts[2].mother.caption=""
    pspicts[3].mother.caption=""

    for psp in pspicts:
        psp.dilatation_X(0.2)
        psp.dilatation_Y(20)

    from scipy import stats

    XX=[]

    XX.append(stats.binom(30,0.9))
    XX.append(stats.binom(30,0.1))
    XX.append(stats.binom(30,0.5))
    XX.append(stats.binom(29,0.5))

    for i,psp in enumerate(pspicts):
        X=XX[i]
        n=X.args[0]
        p=X.args[1]
        for k in range(0,n+1):
            y=X.pmf(k)
            seg=Segment(Point(k,0),Point(k,y))
            seg.parameters.color="blue"
            seg.parameters.add_option("linewidth","1.5mm")
            psp.DrawGraphs(seg)

    for psp in pspicts:
        psp.axes.single_axeX.Dx=5
        psp.axes.single_axeY.Dx=0.05
        psp.axes.do_mx_enlarge=False
        psp.axes.do_my_enlarge=False
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

