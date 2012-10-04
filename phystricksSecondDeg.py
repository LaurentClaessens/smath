from phystricks import *
def SecondDeg():
    pspicts,fig = MultiplePictures("Second",3,script_filename="SecondDeg")
    pspicts[0].mother.caption="Un graphe,"
    pspicts[1].mother.caption="un autre,"
    pspicts[2].mother.caption="et un dernier."


    for psp in pspicts:
        psp.dilatation_Y(0.1)
        psp.dilatation_X(0.4)

    x=var('x')
    mx=-7
    Mx=4
    k=3
    f=phyFunction(x**2+3*x-10)
    g=phyFunction(-x**2-3*x+10)
    h=phyFunction(x**2/k+3*x/k-10/k)

    F=f.graph(mx,Mx)
    G=g.graph(mx,Mx)
    H=h.graph(mx,Mx)

    for psp in pspicts:
        psp.axes.single_axeY.Dx=10
        psp.axes.single_axeX.Dx=2
        psp.DrawDefaultAxes()
        

    pspicts[0].DrawGraphs(F)
    pspicts[1].DrawGraphs(G)
    pspicts[2].DrawGraphs(H)

    fig.conclude()
    fig.write_the_file()
