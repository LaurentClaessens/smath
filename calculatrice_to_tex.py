#! /usr/bin/env python3
# -*- coding: utf8 -*-

def liste_to_latex(l):
    a=[]
    for t in l:
        a.append("\\boxed{"+t+"}")
    return "\,".join(a)

def file_to_latex(filename):
    f=open(filename,'r')
    ops=[x.replace('\n','') for x in f.readlines()]
    f.close()
    return liste_to_latex(ops)

def file_to_file(name):
    text_filename=name+".text"
    calcul_filename=name+".calcul"
    calcul=file_to_latex(text_filename)
    f=open(calcul_filename,'w')
    f.write(calcul)

file_to_file("GKJooPMzPdG")
file_to_file("JPIooEhtUVn")

