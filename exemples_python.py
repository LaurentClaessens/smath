#! /usr/bin/python3
# -*- coding: utf8 -*-

import os

"""
Ce script crée les fichiers de résultats des exemples donnés dans smath.
"""


def resultat(scriptname):
    prompt = "git add {0}.py res_{0}.txt".format(scriptname)
    os.system(prompt)
    prompt = "python3 {0}.py > res_{0}.txt".format(scriptname)
    os.system(prompt)
    print("\lstinputlisting{%s.py}"%scriptname)
    print("donne")
    print("\lstinputlisting[title=Résultat]{res_%s.txt}"%scriptname)
        
        

liste_tests=[
"ex_listes",
"ex_listes2",
"ex_listes3",
"chaussures",
"mediane",
"premier_quartile",
"recurrence2",
"exemple_ceil",
"ex_fonction" ,
"ex_fonction2" ,
"ex_fonction3" ,
"ex_fonction4" ,
"ex_print",
"ex_for1" ,
"ex_join1" ,
"ex_join2" ,
"ex_split1" ,
"ex_triple" ,
"ex_triple2" ,
"ex_texte1",
"ex_texte2"
"ex_texte3",
"ex_graphe"
]

liste_tests=["ex_graphe"]

for res in liste_tests:
    resultat(res)


#resultat("exo_mediane")  # Celui-ci est une cession interactive.
# resultat("recurrence1")     # Celui-ci plante exprès. Alors si on le change, il y a des choses à faire à la main.
# resultat("ex_inverse")    # Celui-ci aussi plante sur un ZeroDivisionError.
