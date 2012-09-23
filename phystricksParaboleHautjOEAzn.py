# -*- coding: utf8 -*-

# Cette figure est seulement utilisée pour son image, pas sa figure. 
# En cas de mise à jour, il faut faire gaffe.
from phystricks import *
def ParaboleHautjOEAzn():
    pspict,fig = SinglePicture("ParaboleHautjOEAzn")
    pspict.dilatation(1)

    x=var('x')

    x=var('x')
    f=phyFunction( (x-3)*(x-1) ).graph(0.5,3.5)
    P=Point(3,0)
    Q=Point(1,0)
    Q.put_mark(0.2,45,"\( x_1\)",automatic_place=pspict)
    P.put_mark(0.2,135,"\( x_2\)",automatic_place=pspict)

    pspict.DrawGraphs(f,P,Q)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.axes.draw_single_axeY=False
    fig.conclude()
    fig.write_the_file()
