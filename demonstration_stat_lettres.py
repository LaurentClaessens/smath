#! /usr/bin/python3.2
# -*- coding: utf8 -*-

import random
import re

texte_fr = """
Qu'est-ce qui se cache derrière ces suites ? Le réchauffement observé pendant plusieurs décennies a été relié aux changements survenus dans le cycle hydrologique à grande échelle, notamment: l'augmentation de la teneur en vapeur d'eau de l'atmosphère, la modification de la configuration, de l'intensité et des extrêmes des précipitations, la diminution de la couverture neigeuse et la fonte des glaces accrue, ainsi que la modification de l'humidité du sol et du ruissellement. """

texte_en="""
Precisely. You allude to my attempt to recover the Irene Adler papers, to the singular case of Miss Mary Sutherland, and to the adventure of the man with the twisted lip. Well, I have no doubt that this small matter will fall into the same innocent category. You know Peterson, the commissionaire?"""

texte_fr_long=open("temps_perdu.txt").read()
texte_en_long=open("Sherlock.txt").read()

def double():
    texte_reference=texte_fr_long
    print(texte_reference,"\n")
    texte_original="at"
    for i in range(1,50):
        derniere=texte_original[-1]
        avant_derniere=texte_original[-2]
        possible=re.compile(re.escape(avant_derniere+derniere)+".").findall(texte_reference)
        print("""Les combinaisons "{}." sont""".format(avant_derniere+derniere),possible)
        choix=random.choice(possible)
        print("""Je choisis "{}" """.format(choix))
        texte_original=texte_original+choix[-1]
        print("Le texte est maintenant :")
        print(texte_original)
        k=input()

def simple():
    texte_reference=texte_fr
    print(texte_reference,"\n")
    texte_original="a"
    for i in range(1,50):
        derniere=texte_original[-1]
        possible=re.compile(re.escape(derniere)+".").findall(texte_reference)
        print("""Les combinaisons "{}." sont""".format(derniere),possible)
        choix=random.choice(possible)
        print("""Je choisis "{}" """.format(choix))
        texte_original=texte_original+choix[-1]
        print("Le texte est maintenant :")
        print(texte_original)
        k=input()

double()
