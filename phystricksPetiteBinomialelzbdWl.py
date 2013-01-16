# -*- coding: utf8 -*-
from phystricks import *
def PetiteBinomialelzbdWl():
    pspicts,fig = MultiplePictures("PetiteBinomialelzbdWl",4)
    pspicts[0].mother.caption="\( n=10\), \( p=0.15\)"
    pspicts[1].mother.caption="\( n=15\), \( p=0.15\)"
    pspicts[2].mother.caption="\( n=10\), \( p=0.85\)"
    pspicts[3].mother.caption="\( n=15\), \( p=0.85\)"

    for psp in pspicts:
        psp.dilatation_X(0.4)
        psp.dilatation_Y(10)

    from scipy import stats

    XX=[]

    XX.append(stats.binom(10,0.15))
    XX.append(stats.binom(15,0.15))
    XX.append(stats.binom(10,0.85))
    XX.append(stats.binom(15,0.85))

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
        psp.axes.single_axeY.Dx=0.1
        psp.axes.do_mx_enlarge=False
        psp.axes.do_my_enlarge=False
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()

