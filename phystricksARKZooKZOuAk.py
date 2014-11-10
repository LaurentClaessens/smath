# -*- coding: utf8 -*-

from phystricks import *
#from LaTeXparser import PytexTools
import LaTeXparser.PytexTools

class Situation(object):
    def __init__(self,name,p1,p2,pts):
        self.name=name
        self.pts=pts
        self.p1=p1
        self.p2=p2
        dic={}
        dic[(0,0)]="\\text{"+p1+"}"
        dic[(0,1)]="\\text{"+p2+"}"
        for i,p in enumerate(pts):
            dic[(i+1,0)]=str(p[0])
            dic[(i+1,1)]=str(p[1])
        self.array=LaTeXparser.PytexTools.Array(dic)
    def write_the_file(self):
        filename="Fig_ARKZooKZOuAk"+self.name+".latex"
        f=open(filename,'w')
        f.write(self.latex())
        f.close()
        print("Tableau dans le fichier",filename)
    def points_list(self):
        return [  Point(k[0],k[1]) for k in self.pts ]
    def latex(self):
        return self.array.latex()

def ARKZooKZOuAk():
    pspict,fig = SinglePicture("ARKZooKZOuAk")
    pspict.dilatation(1)
    
    A=Situation(name="convprix", p1= "prix en euros",p2="prix en wut", pts=[ (1,1.5),(2,3),(3,4.5),(4,6)  ]   )
    A.write_the_file()
    
    pspict.DrawGraphs(A.points_list())
    pspict.DrawDefaultAxes()
    pspict.DrawDefaultGrid()
    fig.conclude()
    fig.write_the_file()
