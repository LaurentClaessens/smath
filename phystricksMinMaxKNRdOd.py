# -*- coding: utf8 -*-
from phystricks import *

def at_max(pspict,P,m,a,o):
    Qa=Point(P.x,0)
    Qa.parameters.symbol="|"
    Qa.put_mark(0.2,m*90,"\( {0}\)".format(a),automatic_place=pspict)
    Qo=Point(0,P.y)
    Qo.parameters.symbol="|"
    Qo.add_option("dotangle=90")
    Qo.put_mark(0.2,90+m*90,"\( {0}\)".format(o),automatic_place=pspict)
    sega=Segment(P,Qa)
    sega.parameters.color="red"
    sega.parameters.style="dotted"

    sego=Segment(P,Qo)
    sego.parameters.color=sega.parameters.color
    sego.parameters.style=sega.parameters.style

    pspict.DrawGraphs(sega,sego,P,Qa,Qo)


def MinMaxKNRdOd():
    pspict,fig = SinglePicture("MinMaxKNRdOd")
    pspict.dilatation(1)

    x=var('x')
    f=HermiteInterpolation([(-2.5,1.3,0),(1,-4,0)]).graph(-4,2)
    f.put_mark(0.2,0,"\( f\)",automatic_place=pspict)

    df=phyFunction(f.sage.diff(x))
    xx=df.inverse(0)

    at_max(pspict,f.get_point(xx[0]),1,"a","M")
    at_max(pspict,f.get_point(xx[1]),-1,"b","m")

    pspict.DrawGraphs(f)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
