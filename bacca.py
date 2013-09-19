#! /usr/bin/sage -python
# -*- coding: utf8 -*-

from __future__ import division

effectifs={0:0,1:0,2:1,3:2,4:2,5:4,6:6,7:5,8:4,9:5,10:11,11:5,12:6,
        13:6,14:5,15:4,16:3,17:5,18:2,19:1,20:0}

nombre_candidats=sum(effectifs.values())
print nombre_candidats

frequences={  i:effectifs[i]/nombre_candidats for i in range(0,21) }

print "La somme des fréquences vaut 1 :",sum(frequence.values())
