# -*- coding: utf8 -*-

def homographique(fun,mx,Mx,interdite,epsilon=0.2):
    f1=phyFunction(fun).graph(mx,interdite-epsilon)
    f2=phyFunction(fun).graph(interdite+epsilon,Mx)
    return f1,f2

from phystricks import *
def OHfdEZt():
    pspicts,fig = MultiplePictures("OHfdEZt",4)
    pspicts[0].mother.caption=""
    pspicts[1].mother.caption=""
    pspicts[2].mother.caption=""
    pspicts[3].mother.caption=""

    epsilon=0.2
    
    for psp in pspicts:
        psp.dilatation_X(0.5)
        psp.dilatation_Y(0.5)

    x=var('x')

    F=[]
    F.append(  homographique(  1/x,-5,5,0  )  )
    F.append(  homographique(  1/(x+2),-7,3,-2  )  )
    F.append(  homographique(  (2*x+3)/(x-1),-7,7,1,epsilon=0.5  )  )
    F.append(  homographique(  (1-x)/(1+x),-4,4,interdite=-1  )  )

    for i,psp in enumerate(pspicts):
        print("===================",i)
        psp.DrawGraphs(F[i])
        psp.DrawDefaultAxes()
        psp.DrawDefaultGrid()


    fig.conclude()
    fig.write_the_file()
