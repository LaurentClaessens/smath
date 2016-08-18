from phystricks import *

def at_droite(pspict,f,color):
    x=var('x')
    mx=-2
    Mx=2
    g=phyFunction(f).graph(mx,Mx)
    g.put_mark(0.2,0,"\( {0}\)".format(latex(g.sage(x))),pspict=pspict)
    P=g.get_point(mx+0.5)
    Q=g.get_point(Mx-0.5)
    g.parameters.color=color
    pspict.DrawGraphs(g,P,Q)

def GrapheAffinHqXJGx():
    pspict,fig = SinglePicture("GrapheAffinHqXJGx")
    pspict.dilatation(1)

    x=var('x')
    at_droite(pspict,x+1,"blue")
    at_droite(pspict,-x+1,"red")
    at_droite(pspict,-2*x,"green")
    at_droite(pspict,3*x/2-1,"cyan")

    pspict.DrawDefaultAxes()
    fig.conclude()
    fig.write_the_file()
