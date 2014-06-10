#! /usr/bin/env python3
# -*- coding: utf8 -*-

# Pas envie de mettre une licence. Prenez la GPL ou la WTFPL.

from __future__ import division
from __future__ import unicode_literals
import codecs
import random

class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "({},{})".format(self.x,self.y)

def randint_non_zero(a,b):
    """
    retourne la même chose que random.randint(a,b), mais exclu la possibilité de sortir un zéro.
    """
    x=0
    while x==0 :
        x=random.randint(a,b)
    return x

def line_equation(A,B):
    """
    Given points A and B, return tuple (a,b,c) such that
    ax+by+c=0
    is the equation of the line AB
    """
    if A.x==B.x:
        return 1,0,-A.x
    b=1
    a=(B.y-A.y)/(A.x-B.x)
    c=-a*A.x-A.y
    return a,b,c

def random_triangle(m,M):
    """
    Return random three points that are not aligned. Coordinates are between m and M
    """
    Ax=random.randint(m,M)
    Ay=random.randint(m,M)
    A=Point(Ax,Ay)
    Bx=A.x
    By=A.y
    while Bx==A.x and By==A.y:
        Bx=random.randint(m,M)
        By=random.randint(m,M)
    B=Point(  Bx,By  )
    # Now choose the third point randomly while the cross product AB x AC is zero
    C=Point( A.x,A.y )
    while (B.y-A.y)*(C.x-A.x)-(B.x-A.x)*(C.y-A.y)==0 :
        Cx=random.randint(m,M)
        Cy=random.randint(m,M)
        C=Point(Cx,Cy)
    return A,B,C

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

def exo_comparer_nombres():
    paires_angles=[]
    paires_angles.append([" \( \pi\)", "\( -\pi\) "])
    paires_angles.append([r"\( \frac{ \pi }{ 4 }\)", r"\( -\frac{ \pi }{ 4 }\) "])
    paires_angles.append([r"\( \frac{ \pi }{ 3 }\)", r"\( \frac{ 2\pi }{ 3 }\) "])
    paires_angles.append([r"\( \frac{ \pi }{ 4 }\)", r"\(  \frac{ 3\pi }{ 4 } \) "])
    paires_angles.append([r"\( \frac{ 10\pi }{ 4 }\)", r"\(  \frac{ 2\pi }{ 4 } \) "])
    paires_angles.append([r"\( \frac{ 10\pi }{ 4 }\)", r"\(  \frac{ 6\pi }{ 4 } \) "])
    paires_angles.append([r"\( \frac{ \pi }{ 2 }\)", r"\( \frac{ 5\pi }{ 2 }\) "])
    paires_angles.append([r"\( \frac{ 2\pi }{ 3 }\)", r"\( -\frac{ 2\pi }{ 3 }\) "])
    paire1=random.choice(paires_angles)
    paire2=paire1
    while paire2==paire1:
        paire2=random.choice(paires_angles)
    paire3=random.choice(paires_angles)
    consigne="""Vrai ou faux ? Vous pouvez justifier par un dessin.
    \\begin{{enumerate}}
    \item
    Les nombres {0} et {1} ont même image sur le cercle trigonométrique.
    \item
    Les nombres {2} et {3} ont même image sur le cercle trigonométrique.
    \end{{enumerate}}
    """.format(paire1[0],paire1[1],paire2[0],paire2[1])
    return consigne,""


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


def exo_distance_ville_trigno():
    lat1=random.randint(1,80)
    lat2=random.randint(1,80)
    NS=random.choice(["nord","sud"])

    consigne=r"""
    La ville V est située à BACKSLASHUnit{{{0}}}{{\degree}} nord tandis que la ville W est située à BACKSLASHUnit{{{1}}}{{\degree}} sud, sur le même méridien. Quelle est la distance entre ces deux villes ? (le rayon de la Terre est approximativement de BACKSLASHUnit{{6300}}{{\kilo\meter}}).
    """.replace("BACKSLASHU","\\u").format(lat1,lat2)
    import math
    reponse=str(2*math.pi*6300*(lat1+lat2)/360)
    return consigne,reponse

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
    # Attention : il faudra rendre cet exercice plus équitable : donner une grande diagonale à tout le monde.
    sommets=["A","B","C","D","E","F","G","H"]
    diags=["AG","EC","FD","BH"]
    d=random.choice(diags)
    p=random.choice(sommets)
    while p in d:
        p=random.choice(sommets)
    pts=d+p
    c=random.randint(14,30)
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
    Quelle est son aire ?
    \end{enumerate}
    """
    return texte,""

def exo_lapins():
    lst=list(range(100,200))
    random.shuffle(lst)
    poids=lst[1:21]
    moyenne=sum(poids)/len(poids)
    nouveau=lst[25]
    texte="""
    Un chercheur en alimentation pour lapin a pesé 20 lapins nains et a obtenu les poids suivants """+", ".join( [str(x) for x in poids] )+""". La moyenne des poids est de {} """.format(str(moyenne)[0:6])+" grammes. En dernière minute son assistant lui fait remarquer une erreur de mesure sur le dernier lapin pesé (celui de \\unit{"+str(poids[-1])+"}}{{\gram}}) : en réalité il pèse {} grammes. Quelle est la nouvelle moyenne ?".format(nouveau)
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

def exo_parallelogramme():
    """
    Donne trois points non alignés et demande le quatrième donnant un parallélogramme.
    """
    A,B,C=random_triangle(-10,10)
    pts=["A","B","D","E","F","K","L","M"]
    random.shuffle(pts)
    texte="""
    Soient les points ${}({};{})$, ${}({};{})$ et ${}({};{})$. Donner les coordonnées du point ${}$ tel que ${}{}{}{}$ soit un parallélogramme (méthode au choix).
    """.format(pts[0],A.x,A.y,pts[1],B.x,B.y,pts[2],C.x,C.y,pts[3],pts[0],pts[1],pts[2],pts[3])
    Dx=A.x+C.x-B.x
    Dy=A.y+C.y-B.y
    reponse = "${}=({};{})$".format(pts[3],Dx,Dy)
    return texte,reponse

def exo_coord_vecteur():
    """
    Donne deux points et demande les coordonnées du vecteur
    """
    A,B,C=random_triangle(-10,10)
    texte=r"""Soient les points $A({};{})$, $ B({},{})$ et $ C({};{})$. 
    \begin{{enumerate}}
    \item
    
    Calculer les coordonnées des vecteurs \( \vect{{ AB }}\) et \( \vect{{ AB }}+\vect{{ BC }}\). 

\item
    Donner les coordonnées du point \( X\) tel que \( \vect{{ AX }}=\vect{{ BC }}\) (méthode au choix)
    \end{{enumerate}}
    
    """.format(A.x,A.y,B.x,B.y,C.x,C.y)
    AB=Point(B.x-A.x,B.y-A.y)
    BC=Point(C.x-B.x,C.y-B.y)
    reponse=r"""

    $\vect{{ AB }}=({};{})$

    $\vect{{ AB }}+\vect{{ BC }}=({};{})$

    $X=({};{})$
    """.format(   AB.x,AB.y,  AB.x+BC.x,AB.y+BC.y,A.x+BC.x,A.y+BC.y    )
    return texte,reponse

class Sujet(object):
    def __init__(self,name):
        self.name=name
        self.texfile=codecs.open(name+".tex","w",encoding="utf8") # c'est le fichier qui sera à compiler
        self.sujet=""
        self.correction=""
    def double_write(self,x):
        self.sujet=self.sujet+x
        self.correction=self.correction+x
    def ecrit_un_exo(self,fun,itemize=True):
        texte,reponse=fun()
        if itemize :
            self.double_write("\item\n")
        self.double_write(texte)
        self.correction=self.correction+"\n\n"
        self.correction=self.correction+reponse
        self.sujet=self.sujet+"\n"
    def ecrit_sujet(self,liste_exo,i,random_order=False):
        if random_order: 
            random.shuffle(liste_exo)
        self.double_write("\\vbox{")
        self.double_write("Numéro "+str(i)+"."+"\n"+"\\emph{Toutes les réponses doivent être justifiées par un calcul accompagné d'un raisonnement.}\n")
        if len(liste_exo)>1:
            self.double_write(r"\begin{enumerate}")
        for fun in liste_exo:
            self.ecrit_un_exo(fun,itemize=len(liste_exo)>1)
        self.double_write("\n")
        if len(liste_exo)>1:
            self.double_write("""\end{enumerate}\n""")
        self.double_write("}")
        self.sujet=self.sujet+"\n\\vspace{2cm}\n"
        self.correction=self.correction+"\n"
    def close(self):
        generic=codecs.open("generic_interro.tex",encoding="utf8").read()
        a=[]
        a.append(self.sujet)
        a.append("\section{correction}")
        a.append(self.correction)
        non_generic_latex="\n".join(a)
        code=generic.replace("LES QUESTIONS",non_generic_latex)
        print("J'écris le fichier",self.name+".tex")
        self.texfile.write(code)
        self.texfile.close()

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
    sujet=Sujet("interro_geometrie_espace")
    liste_exo=[exo_cube]
    for i in range(1,41):
        sujet.ecrit_sujet(liste_exo,i)
    sujet.close()

def interro_statistique_descriptive():
    sujet=Sujet("interro_statistique_descriptive")
    for i in range(1,41):
        liste_exo=[exo_lapins,exo_ECC]
        sujet.ecrit_sujet(liste_exo,i)
    sujet.close()

def interro_vecteurs():
    sujet=Sujet("interro_vecteurs")
    for i in range(1,75):
        liste_exo=[exo_parallelogramme,exo_coord_vecteur]
        sujet.ecrit_sujet(liste_exo,i,random_order=True)
    sujet.close()


def interro_trigono():
    sujet=Sujet("interro_trigono")
    for i in range(1,40):
        liste_exo=[exo_comparer_nombres,exo_distance_ville_trigno]
        sujet.ecrit_sujet(liste_exo,i,random_order=True)
    sujet.close()

interro_trigono()
