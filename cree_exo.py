#! /usr/bin/env python3
# -*- coding: utf8 -*-

# Pas envie de mettre une licence. Prenez la GPL ou la WTFPL.

from __future__ import division
from __future__ import unicode_literals
import codecs
import random

def randint_non_zero(a,b):
    """
    retourne la même chose que random.randint(a,b), mais exclu la possibilité de sortir un zéro.
    """
    x=0
    while x==0 :
        x=random.randint(a,b)
    return x

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

def interro_trig2():
    paires_angles=[]
    paires_angles.append([" \( \pi\)", "\( -\pi\) "])
    paires_angles.append([r"\( \frac{ \pi }{ 4 }\)", r"\( -\frac{ \pi }{ 4 }\) "])
    paires_angles.append([r"\( \frac{ \pi }{ 3 }\)", r"\( \frac{ 2\pi }{ 3 }\) "])
    paires_angles.append([r"\( \frac{ \pi }{ 4 }\)", r"\(  \frac{ 3\pi }{ 4 } \) "])
    paires_angles.append([r"\( \frac{ 10\pi }{ 4 }\)", r"\(  \frac{ 2\pi }{ 4 } \) "])
    paires_angles.append([r"\( \frac{ 10\pi }{ 4 }\)", r"\(  \frac{ 6\pi }{ 4 } \) "])
    paires_angles.append([r"\( \frac{ \pi }{ 2 }\)", r"\( \frac{ 5\pi }{ 2 }\) "])
    paires_angles.append([r"\( \frac{ 2\pi }{ 3 }\)", r"\( -\frac{ 2\pi }{ 3 }\) "])
    paires_angles.append([r"\( \frac{ 2\pi }{ 5 }\)", r"\( -\frac{ 2\pi }{ 5 }\) "])
    operations=["sin","cos"]
    paire1=random.choice(paires_angles)
    op1=random.choice(operations)
    op2=random.choice(operations)
    lat1=random.randint(1,80)
    lat2=random.randint(1,80)
    lat3=random.randint(1,80)
    NS=random.choice(["nord","sud"])

    op1=op2 # Ici je demande qu'on ne compare pas sin et cos.

    consigne=r"""
    \vbox{{
    NUM. Vous pouvez justifier les réponses aux questions suivantes par un dessin et un petit calcul.
    \begin{{enumerate}}
    \item
    La ville V est située à BACKSLASHUnit{{{4}}}{{\degree}} nord tandis que la ville W est située à BACKSLASHUnit{{{5}}}{{\degree}} sud, sur le même méridien. Quelle est la distance entre ces deux villes ? (le rayon de la Terre est approximativement de BACKSLASHUnit{{6300}}{{\kilo\meter}}).
    \item
    Quel est le rayon de la «tranche»  horizontale de la Terre à BACKSLASHUnit{{{6}}}{{\degree}} {7} ?
    \item
    Vrai ou faux : {0}({1})={2}({3}) ?
    \end{{enumerate}}
    }}
    \vspace{{1.5cm}}
    """.replace("BACKSLASHU","\\u").format(op1,paire1[0],op1,paire1[1],lat1,lat2,lat3,NS)
    return consigne


def exo_repere_milieu_distance():
    Ax=random.randint(-10,10)
    Bx=random.randint(-10,10)
    Cx=random.randint(-10,10)
    Dx=random.randint(-10,10)
    Ay=random.randint(-10,10)
    By=random.randint(-10,10)
    Cy=random.randint(-10,10)
    Dy=random.randint(-10,10)
    texte=r"""Placer les points \( A=({};{})\), \( B=({};{})\), \( C=({};{})\) et \( D=({};{})\) dans un repère orthonormé. Calculer la longueur du segment \( [AB]\) et les coordonnées du milieu du segment \( [CD]\).""".format(Ax,Ay,Bx,By,Cx,Cy,Dx,Dy)
    lsq=(Ax-Bx)**2+(Ay-By)**2
    l=sqrt(lsq)
    Mx=(Cx+Dx)/2
    My=(Cy+Dy)/2
    reponse=" $l^2={}$,$l={}$,$M=({},{})$".format(lsq,l,Mx,My)
    return texte,reponse

def exo_isocele():
    on=random.choice([True,False])
    xA=random.randint(-10,10)
    yA=random.randint(-10,10)
    k=randint_non_zero(-3,3)
    r=randint_non_zero(-4,4)
    xB=xA-2*k
    yB=yA+2*k
    xM=int((xA+xB)/2)
    yM=int((yA+yB)/2)
    xC=xM+r
    yC=yM+r
    if not on :
        xC=xC+10
    texte="""Est-ce que le triangle formé par les points \( A({};{})\), \( B({};{})\) et \( C({};{})\) est isocèle ?""".format(xA,yA,xB,yB,xC,yC)
    reponse = on
    return texte,str(reponse)

def exo_rectangle():
    # Pour la prochaine fois, il faudrait que l'on demande si il est rectangle en tel point.
    on=random.choice([True,False])
    xA=random.randint(-10,10)
    yA=random.randint(-10,10)
    k=randint_non_zero(-5,5)
    r=randint_non_zero(-3,3)
    xB=xA-k
    yB=yA+k
    xC=xA+r
    yC=yA+r
    if not on :
        xC=xC+10
    texte="""Est-ce que le triangle formé par les points \( A({};{})\), \( B({};{})\) et \( C({};{})\) est rectangle ?""".format(xA,yA,xB,yB,xC,yC)
    reponse = on
    return texte,str(reponse)

def exo_cube():
    pts=["A","B","C","D","E","F","G","H"]
    random.shuffle(pts)
    c=random.randint(2,7)
    texte=r"""
\begin{wrapfigure}{r}{5.0cm}
   \vspace{-0.5cm}        % à adapter.
   \centering
   \input{Fig_OKTXHoc.pstricks}
\end{wrapfigure}

    La figure ci-contre est un cube de \unit{"""+str(c)+r"""}{\centi\meter}.

    \begin{enumerate}
    \item
    Quelle est la nature du triangle \("""+"{}{}{}".format(pts[0],pts[1],pts[2])+r"""\) ? 
    \item
    Quel est son périmètre ?
    \item
    Quelle est son aire ? (pour les rapides)
    \end{enumerate}
    """
    return texte,""

def exo_lapins():
    lst=list(range(100,200))
    random.shuffle(lst)
    poids=lst[1:16]
    moyenne=sum(poids)/len(poids)
    nouveau=lst[20]
    texte="""
    Un chercheur en alimentation pour lapin a pesé 15 lapins nains et a obtenu les poids suivants """+", ".join( [str(x) for x in poids] )+""". La moyenne des poids est de {} """.format(str(moyenne)[0:6])+" grammes. En dernière minute son assistant lui fait remarquer une erreur de mesure sur le dernier lapin pesé : en réalité il pèse {} grammes. Quelle est la nouvelle moyenne ?".format(nouveau)
    reponse=(moyenne+(nouveau-poids[-1]))/len(poids)
    return texte,str(reponse)

def exo_ECC():
    e=[   random.randint(1,15) for i in range(0,5)  ]
    c=[   sum(e[:i]) for i in range(1,len(e)+1)  ]

    texte=r"""Compléter le tableau suivant :
        \begin{equation*}
        \begin{array}[]{|c||c|c|c|c|c|}
        \hline
        \text{Valeur}&1000&1200&1300&1400&1500\\
                \hline"""+"\\text{{Effectifs}}&{}&&{}&{}&{}\\\\\\hline".format(e[0],e[2],e[3],e[4])+"\\text{{ECC}}&{}&{}&{}&&{}\\\\".format(c[0],c[1],c[2],c[4])+r"""\hline
                                \end{array}
                                \end{equation*}
        """
    reponse=str(e)+"\\"+str(c)
    return texte,reponse

class double_write(object):
    def __init__(self,f1,f2):
        self.f1=f1
        self.f2=f2
    def write(self,text):
        self.f1.write(text)
        self.f2.write(text)

def ecrit_un_exo(f_sujet,f_correction,fun,itemize=True):
    X=double_write(f_sujet,f_correction)
    texte,reponse=fun()
    if itemize :
        X.write("\item\n")
    X.write(texte)
    f_correction.write("\n\n")
    f_correction.write(reponse)
    f_sujet.write("\n")

def ecrit_sujet(f_sujet,f_correction,liste_exo,i):
    #random.shuffle(liste_exo)
    X=double_write(f_sujet,f_correction)
    X.write("\\vbox{")
    X.write(str(i)+"\n"+"\\emph{Toutes les réponses doivent être justifiées par un calcul accompagné d'un raisonnement.}\n")
    #X.write(str(i))
    if len(liste_exo)>1:
        X.write(r"\begin{enumerate}")
    for fun in liste_exo:
        ecrit_un_exo(f_sujet,f_correction,fun,itemize=len(liste_exo)>1)
    X.write("\n")
    if len(liste_exo)>1:
        X.write("""\end{enumerate}\n""")
    X.write("}")
    f_sujet.write("\n\\vspace{2cm}\n")
    f_correction.write("\n")

def interro_repere_distance_milieu():
    f_sujet=codecs.open("interro_repere_distance_sujet.tex","w",encoding="utf8")
    f_correction=codecs.open("interro_repere_distance_correction.tex","w",encoding="utf8")
    for i in range(1,85):
        liste_exo=[]
        liste_exo.append(exo_repere_milieu_distance)
        ir=random.randint(0,1)
        if ir==0:
            liste_exo.append(exo_isocele)
        else :
            liste_exo.append(exo_rectangle)
        ecrit_sujet(f_sujet,f_correction,liste_exo,i)
    f_sujet.close()
    f_correction.close()

def interro_geometrie_espace():
    f_sujet=codecs.open("interro_geometrie_espace_sujet.tex","w",encoding="utf8")
    f_correction=codecs.open("interro_geometrie_espace_correction.tex","w",encoding="utf8")
    for i in range(1,41):
        liste_exo=[exo_cube]
        ecrit_sujet(f_sujet,f_correction,liste_exo,i)
    f_sujet.close()
    f_correction.close()

def interro_statistique_descriptive():
    f_sujet=codecs.open("interro_statistique_descriptive_sujet.tex","w",encoding="utf8")
    f_correction=codecs.open("interro_statistique_descriptive_correction.tex","w",encoding="utf8")
    for i in range(1,41):
        liste_exo=[exo_lapins,exo_ECC]
        ecrit_sujet(f_sujet,f_correction,liste_exo,i)
    f_sujet.close()
    f_correction.close()

interro_statistique_descriptive()
