from phystricks import *
def ParaboleBasfKtFCN():
    pspict,fig = SinglePicture("ParaboleBasfKtFCN")
    pspict.dilatation(1)

    x=var('x')
    f=phyFunction( -((x+3)-3)*((x+3)-1) ).graph(-2.5,0.5)
    g=f.sage.expand()
    a=g.coefficient(x,2)
    b=g.coefficient(x,1)
    c=g.coefficient(x,0)
    x0=-b/(2*a)
    P=Point(x0,0)
    P.put_mark(0.2,90,"\( x_0\)",pspict=pspict)

    pspict.DrawGraphs(f,P)
    pspict.axes.no_graduation()
    pspict.DrawDefaultAxes()

    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
