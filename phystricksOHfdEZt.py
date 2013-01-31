# -*- coding: utf8 -*-

def homographique(fun,mx,Mx,interdite,epsilon=0.2):
    f1=phyFunction(fun).graph(mx,interdite-epsilon)
    f2=phyFunction(fun).graph(interdite+epsilon,Mx)
    return f1,f2

from phystricks import *
def OHfdEZt():
    pspicts,fig = MultiplePictures("OHfdEZt",6)
    pspicts[0].mother.caption="<+caption1+>"
    pspicts[1].mother.caption="<+caption2+>"
    pspicts[2].mother.caption="<+caption3+>"
    pspicts[3].mother.caption="<+caption3+>"
    pspicts[4].mother.caption="<+caption3+>"
    pspicts[5].mother.caption="<+caption3+>"

    epsilon=0.2
    
    for psp in pspicts:
        psp.dilatation_X(0.5)
        psp.dilatation_Y(0.5)

    x=var('x')

    F=[]
    F.append(  homographique(  1/x,-5,5,0  )  )
    F.append(  homographique(  1/(x+2),-3,7,-2  )  )
    F.append(  homographique(  (2*x+3)/(x-1),-5,5,1  )  )
    F.append(  homographique(  (1-x)/(1+x),-3,3,interdite=-1  )  )
    F.append(  homographique(  (2-2*x)/(5*x+7),-5,5,interdite=-7/5,epsilon=1  )  )
    F.append(  homographique(  (x+3)/(4-2*x),-5,5,interdite=2  )  )

    for i,psp in enumerate(pspicts):
        print("===================",i)
        psp.DrawGraphs(F[i])
        psp.DrawDefaultAxes()
        psp.DrawDefaultGrid()


    fig.conclude()
    fig.write_the_file()
