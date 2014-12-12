from __future__ import division
from phystricks import *

def Secteur(circle,a,b):
    P=circle.get_point(a)
    Q=circle.get_point(b)
    l1=Segment( circle.center,P  )
    l2=circle.graph(a,b)
    l3=Segment(Q,circle.center)
    return CustomSurface(l1,l2,l3)
     
def lignes(n):
    O=Point(0,0)
    cercle=Circle(O,1)
    import numpy
    l=[]
    for a in numpy.linspace(0,360,n,endpoint=False):
        s=Segment(  cercle.get_point(a),O  )
        s.parameters.style="dashed"
        l.append(s)
    return l

