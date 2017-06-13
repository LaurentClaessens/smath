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

def thales(A,B,C,prop,ma,mb,mc,mi,mj,pspict,rotate=0):
    trig=Polygon(A,B,C)
    trig.put_mark(0.2,text_list=["\( {}\)".format(ma),"\( {}\)".format(mb),"\( {}\)".format(mc)],pspict=pspict)
    I=Segment(A,C).get_point_proportion(prop)
    J=Segment(A,B).get_point_proportion(prop)
    I.put_mark(0.2,I.advised_mark_angle(pspict),added_angle=rotate,text="\( {}\)".format(mi),pspict=pspict,position="corner")
    J.put_mark(0.2,J.advised_mark_angle(pspict),added_angle=180+rotate,text="\( {}\)".format(mj),pspict=pspict,position="corner")
    seg=Segment(I,J)
    pspict.DrawGraphs(trig,seg,I,J)
    return I,J

def parallelog(A,B,C,points_names="ABCD",fig=None,pspict=None):
    D=A+C-B
    parall=Polygon(A,B,C,D)
    parall.put_mark(0.2,points_names=points_names,pspict=pspict)

    s1=Segment(A,B)
    s2=Segment(B,C)
    s1.parameters.style="dashed"

    no_symbol(parall.vertices)

    pspict.DrawGraphs(s1,s2,parall.vertices[:-1])

    pspict.math_BB.append(D,pspict=pspict)
    pspict.math_BB.xmax+=1
    pspict.math_BB.ymax+=1
    pspict.math_BB.xmin-=1
    pspict.math_BB.ymin-=1

    pspict.DrawDefaultGrid()
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()

def petit(x,y,color="lightgray"):
    color="lightgray"
    rect=Rectangle(  Point(x,y),Point(x+1,y+1) )
    rect.parameters.filled()
    rect.parameters.fill.color=color
    return rect

def contour(n,pspict):
    for k in range(0,n):      # Le haut et le bas
        pspict.DrawGraphs( petit(k,0,color="red"),petit(k,n-1,color="red") )
    for k in range(1,n-1):        # La gauche et la droite
        pspict.DrawGraphs( petit(0,k,color="green"),petit(n-1,k,color="green") )

def petitAKL(x,y):
    return Rectangle(  Point(x,y+1),Point(x+1,y) )
