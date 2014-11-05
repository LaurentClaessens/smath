# -*- coding: utf8 -*-

from phystricks import *
#from LaTeXparser import PytexTools
import LaTeXparser.PytexTools

class Situation(object):
    def __init__(self,p1,p2,pts):
        self.pts=pts
        self.p1=p1
        self.p2=p2
        self.array=LaTeXparser.PytexTools.Array(self.p1,self.p2,pts)
    def latex(self):
        return self.array.latex()
        


def ARKZooKZOuAk():
    pspict,fig = SinglePicture("ARKZooKZOuAk")
    pspict.dilatation(1)
    
    A=Situation(['14','15'],["prix F","prix E"],  {  (1,1):'a',(2,1):'b',(1,2):"c",(2,2):"d"  }   )
    print(A.latex())

    #pspict.DrawGraphs()
    #pspict.DrawDefaultAxes()
    #fig.conclude()
    #fig.write_the_file()
