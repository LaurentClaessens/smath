# -*- coding: utf8 -*-
from phystricks import *
def ParaboleHautMLbPQF():
    print u"Cette fonction n'est utilisée que pour la pspicture qui est inclue par \includegraphics. En cas de bug, il faut faire des trucs à la main."
    pspict,fig = SinglePicture("ParaboleHautMLbPQF")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction( (x-3)*(x-1) ).graph(0.5,3.5)
    g=f.sage.expand()
    a=g.coefficient(x,2)
    b=g.coefficient(x,1)
    c=g.coefficient(x,0)
    x0=-b/(2*a)
    P=Point(x0,0)
    P.put_mark(0.2,90,"\( x_0\)",automatic_place=pspict)

    pspict.DrawGraphs(f,P)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
