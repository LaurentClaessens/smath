#! /usr/bin/python3
# -*- coding: utf8 -*-

import os

for f in os.listdir('.'):
    if f.endswith(".png"):
        png=f
        pdf=f.replace("png",'pdf')
        if " " in f :
            print("Un espace dans un nom de fichier ??")
        commande_e="convert "+png+" "+pdf
        print(commande_e)
        os.system(commande_e)
