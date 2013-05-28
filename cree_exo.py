#! /usr/bin/env python3
# -*- coding: utf8 -*-

import random

def aff():
    a=random.randint(1,9)
    b=random.randint(1,9)
    types=["ax+b","ax-b","b-ax"]
    s=random.choice(types)
    return s.replace("a",str(a)).replace("b",str(b)).replace("1x","x")

def lin():
    a=random.randint(1,9)
    types=["ax","-ax"]
    s=random.choice(types)
    return s.replace("a",str(a)).replace("1x","x")

def expression():
    types=["A+(A)(B)","(A)(B)+A","C(A)+(A)(B)","(B)(A)+C(A)"]
    A=aff()
    B=aff()
    C=lin()
    s=random.choice(types)
    #print(s,A,B,C)
    return s.replace("A",A).replace("B",B).replace("C",C).replace("+-","-")

def exo():
    consigne="""Factoriser l'expression $EXPRESSION$. Pour quelle valeur de \( x\) est-elle nulle ?
    \\vspace{2cm}
    """
    exp=expression()
    return consigne.replace("EXPRESSION",exp)

for i in range(1,40):
    print("{}.".format(i),exo())
