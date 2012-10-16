from phystricks import *
def ParaboleUniqueBaskGdqda():
    pspict,fig = SinglePicture("ParaboleUniqueBaskGdqda")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction(-(x/1.5)**2).graph(-2,2)
    P=Point(0,0)
    P.put_mark(0.2,90,"\( x_0\)",automatic_place=pspict)

    pspict.DrawGraphs(f,P)
    pspict.axes.no_graduation()
    pspict.axes.draw_single_axeY=False
    pspict.DrawDefaultAxes()

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
