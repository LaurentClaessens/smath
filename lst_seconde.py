#! /usr/bin/python
# -*- coding: utf8 -*-

import LaTeXparser
import LaTeXparser.PytexTools

myRequest = LaTeXparser.PytexTools.Request("seconde")
myRequest.original_filename="smath.tex"

myRequest.ok_filenames_list=["e_smath","seconde","second_deg","repere","equationDroites","fonctions","stat_Pauline","exercices_stats_descriptives","calcul_mental","rappels_geom","perspective","vecteurs","algo","ineqs","affines","IFetIC"]
