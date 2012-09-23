from phystricks import *
import math
def MathCeilwCXIJZ():
    pspict,fig = SinglePicture("MathCeilwCXIJZ")
    pspict.dilatation(1)

    x=var('x')
    for i in range(1,15):
        P=Point(i,math.ceil(i/4))
        P.parameters.color="blue"
        pspict.DrawGraphs(P)

    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
