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

def exo_facto():
    consigne="""Factoriser l'expression $EXPRESSION$. Pour quelle valeur de \( x\) est-elle nulle ?
    \\vspace{2cm}
    """
    exp=expression()
    return consigne.replace("EXPRESSION",exp)

def exo_trig():
    paires_angles=[]
    paires_angles.append([" \( \pi\)", "\( -\pi\) "])
    paires_angles.append([r"\( \frac{ \pi }{ 4 }\)", r"\( -\frac{ \pi }{ 4 }\) "])
    paires_angles.append([r"\( \frac{ \pi }{ 3 }\)", r"\( \frac{ 2\pi }{ 3 }\) "])
    paires_angles.append([r"\( \frac{ \pi }{ 4 }\)", r"\(  \frac{ 3\pi }{ 4 } \) "])
    paires_angles.append([r"\( \frac{ 10\pi }{ 4 }\)", r"\(  \frac{ 2\pi }{ 4 } \) "])
    paires_angles.append([r"\( \frac{ 10\pi }{ 4 }\)", r"\(  \frac{ 6\pi }{ 4 } \) "])
    paires_angles.append([r"\( \frac{ \pi }{ 2 }\)", r"\( \frac{ 5\pi }{ 2 }\) "])
    paires_angles.append([r"\( \frac{ 2\pi }{ 3 }\)", r"\( -\frac{ 2\pi }{ 3 }\) "])
    operations=["sin","cos"]
    paire1=random.choice(paires_angles)
    paire2=paire1
    while paire2==paire1:
        paire2=random.choice(paires_angles)
    paire3=random.choice(paires_angles)
    op1=random.choice(operations)
    op2=random.choice(operations)
    op1=op2 # Ici je demande qu'on ne compare pas sin et cos.
    consigne="""Vrai ou faux ? Vous pouvez justifier par un dessin.
    \\begin{{enumerate}}
    \item
    Les nombres {0} et {1} ont même image sur le cercle trigonométrique.
    \item
    Les nombres {2} et {3} ont même image sur le cercle trigonométrique.
    \item
    {4}({5})={6}({7})
    \end{{enumerate}}
    \\vspace{{2cm}}
    """.format(paire1[0],paire1[1],paire2[0],paire2[1],op1,paire3[0],op2,paire3[1])
    return consigne

def exo_ineqs():
    p1=aff()
    p2=aff()
    liste_sens=["<",">","\leq","\geq"]
    sens=random.choice(liste_sens)
    ineq="({0})({1}){2}0".format(p1,p2,sens)
    type_eqa=["\\frac{ 1 }{ A}=\\frac{ B }{ (A)(C) }","\\frac{ B }{ (A)(C) }=\\frac{1}{ A }"]
    eqa_gen=random.choice(type_eqa)
    A=aff()
    B=lin()
    C=aff()
    eqa=eqa_gen.replace("A",A).replace("B",B).replace("C",C)
    consigne="""Résoudre en justifiant les étapes.
    \\begin{{enumerate}}
    \item
    \( {0}\)
    \item
    \( {1}\)
    \end{{enumerate}}
    \\vspace{{2cm}}
    """.format(ineq,eqa)
    return consigne


for i in range(1,40):
    print("{0}.".format(i),exo_ineqs())

