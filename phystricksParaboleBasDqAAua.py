from phystricks import *
def ParaboleBasDqAAua():
    pspict,fig = SinglePicture("ParaboleBasDqAAua")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction( -((x+3)-3)*((x+3)-1) ).graph(-2.5,0.5)

    P=Point(-2,0)
    Q=Point(0,0)
    P.put_mark(0.2,135,"\( x_1\)",automatic_place=pspict)
    Q.put_mark(0.2,45,"\( x_2\)",automatic_place=pspict)

    pspict.DrawGraphs(f,P,Q)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()
    pspict.axes.draw_single_axeY=False

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
