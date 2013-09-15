# -*- coding: utf8 -*-

from __future__ import division

from phystricks import *
def LNfaWPF():
    pspict,fig = SinglePicture("LNfaWPF")
    pspict.dilatation(1)


    tableau="""
-,-,-2,3,i,-,-,-,-
-,-,1,-,-,i,-,-,i
-,i,i,i,-,i,-,-,-3
-,i,-,-,2,-,-,i,i
i,-,-4,i,-,-,-3,-,1
i,2,-,i,i,-,0,-,i
i,-,i,-,1,-,-,i,i
-,i,-,-,-2,i,-,-,0
i,3,-,-,i,-3,i,-,-
"""

    l=1
    vlines=[]
    hlines=[]
    content=[]
    numbering=[]

    import string
    for i in range(0,9):
        A=Point(  (i+1)*l-l/2,l/2  )
        A.parameters.symbol="none"
        A.put_mark(0,0,string.uppercase[i])
        B=Point(-l/2,-i*l-l/2)
        B.parameters.symbol="none"
        B.put_mark(0,0,string.digits[i+1])
        numbering.append(A)
        numbering.append(B)

    for i in range(0,10):
        v=Segment(Point(i*l,0),Point(i*l,-9*l))
        h=Segment(Point(0,-i*l),Point(9*l,-i*l))
        if i%3==0 :
            #v.parameters.color="red"
            #h.parameters.color="blue"
            v.parameters.add_option("linewidth","0.07cm")
            h.parameters.add_option("linewidth","0.07cm")
        vlines.append(v)
        hlines.append(h)

    
    lines = tableau.split("\n")[1:]
    for i,li in enumerate(lines):
        for j,c in enumerate(li.replace(" ","").split(",")):
            A=Point(   j*l+l/2, -i*l-l/2  )
            A.parameters.symbol="none"
            if c=="i":
                A.put_mark(3*l/9,-90,"\ldots",automatic_place=(pspict,"N"))
            if c in [  str(k) for k in range(-9,10)  ] :
                A.put_mark(0,0,c)
            content.append(A)

    pspict.DrawGraphs(vlines,hlines,content,numbering)
    fig.conclude()
    fig.write_the_file()
