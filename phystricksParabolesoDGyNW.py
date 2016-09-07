from phystricks import *
def ParabolesoDGyNW():
    pspicts,fig = MultiplePictures("ParabolesoDGyNW",4)
    pspicts[0].mother.caption="Une parabole"
    pspicts[1].mother.caption="Une parabole"
    pspicts[2].mother.caption="Une parabole"
    pspicts[3].mother.caption="Une parabole"


    for psp in pspicts:
        psp.dilatation_Y(0.7)
        psp.dilatation_X(0.7)

    x=var('x')
    f=[]
    f.append( phyFunction(8*(x+1)*(x-2)/9).graph(-2,3) )
    f.append( phyFunction((x+2)**2).graph(-4,0) )
    f.append( phyFunction((x-3)**2-1).graph(1,5) )
    f.append( phyFunction((-4/9)*(x-1)*(x-4)).graph(0,5) )

    for i,psp in enumerate(pspicts):
        psp.DrawGraphs(f[i])
        psp.DrawDefaultGrid()
        psp.DrawDefaultAxes()

    fig.conclude()
    fig.write_the_file()
