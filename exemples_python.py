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


resultat("ex_listes")
resultat("ex_listes2")
resultat("ex_listes3")
resultat("chaussures")
resultat("mediane")
resultat("premier_quartile")
resultat("recurrence2")  
resultat("exemple_ceil")  

#resultat("exo_mediane")  # Celui-ci est une cession interactive.
# resultat("recurrence1")     # Celui-ci plante exprès. Alors si on le change, il y a des choses à faire à la main.
