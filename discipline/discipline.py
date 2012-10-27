#! /usr/bin/python3.2
# -*- coding: utf8 -*-

import locale
import datetime
locale.setlocale(locale.LC_ALL,"")

class Croix(object):
    def __init__(self,jour,mois,an,motif):
        self.datetime=datetime.datetime(an,mois,jour,12,12)
        self.motif=motif+" le "+self.datetime.strftime("%A %d %B %Y")

class Colle(object):
    def __init__(self,jour,mois,an,motif,nom,prenom):
        self.datetime=datetime.datetime(an,mois,jour,12,12)
        self.nom=nom
        self.prenom=prenom
        self.motif=motif
    def __str__(self):
        a=[]
        a.append("Colle pour {0} {1} le {2}".format(self.nom,self.prenom,self.datetime.strftime("%A %d %B %Y")))
        a.append(self.motif)
        return '\n'.join(a)

class Student(object):
    def __init__(self,groupe=""):
        self.groupe=groupe
        self.croix=[]
        self.old_croix=[]
        self.colles=[]
        self.nom=""
        self.prenom=""
    def append_bar(self,jour,mois,an,motif):
        self.croix.append(Croix(jour,mois,an,motif))
    def append_colle(self,jour,mois,an,motif=None,extra=False):
        """
        Si on ne donne pas de motifs, c'est les croix obtenues jusqu'alors.

        Le paramètre 'extra' dit si c'est une colle en plus des croix.
        """
        self.old_croix.extend(self.croix)
        if motif==None:
            motif="\n".join([x.motif for x in self.croix])
        self.colles.append(Colle(jour,mois,an,motif,nom=self.nom,prenom=self.prenom))
        if not extra:
            self.croix=[]

seconde_deux={}
seconde_deux[("Atzorivenne","Mathis")]=Student(groupe="2nd2")
seconde_deux[("Bailly","Thomas")]=Student(groupe="2nd2")
seconde_deux[("Bauche","Léa")]=Student(groupe="2nd2")
seconde_deux[("Besancon","Séphora")]=Student(groupe="2nd2")
seconde_deux[("Besnier","Romain")]=Student(groupe="2nd2")
seconde_deux[("Blanchot","Noé")]=Student(groupe="2nd2")
seconde_deux[("Caretti","Arno")]=Student(groupe="2nd2")
seconde_deux[("Colin","Mathieu")]=Student(groupe="2nd2")
seconde_deux[("Dole","Cynthia")]=Student(groupe="2nd2")
seconde_deux[("Dominot","Charline")]=Student(groupe="2nd2")
seconde_deux[("Giroux","Adeline")]=Student(groupe="2nd2")
seconde_deux[("Gras","Guillaume")]=Student(groupe="2nd2")
seconde_deux[("Guenard","Florian")]=Student(groupe="2nd2")
seconde_deux[("Guillot","Anthony")]=Student(groupe="2nd2")
seconde_deux[("Koehler","Paul-Erwan")]=Student(groupe="2nd2")
seconde_deux[("Kuti","Belinda")]=Student(groupe="2nd2")
seconde_deux[("Larderet","Etienne")]=Student(groupe="2nd2")
seconde_deux[("Letondor-Lavrut","Claire")]=Student(groupe="2nd2")
seconde_deux[("Limoge","Thibaut")]=Student(groupe="2nd2")
seconde_deux[("Mougeot","Romain")]=Student(groupe="2nd2")
seconde_deux[("Navel","Rémi")]=Student(groupe="2nd2")
seconde_deux[("Pardon","Mélanie")]=Student(groupe="2nd2")
seconde_deux[("Perrault","Mélanie")]=Student(groupe="2nd2")
seconde_deux[("Pillot","César")]=Student(groupe="2nd2")
seconde_deux[("Préaud","Raphaël")]=Student(groupe="2nd2")
seconde_deux[("Robert","Jérémy")]=Student(groupe="2nd2")
seconde_deux[("Tépinier","Laura")]=Student(groupe="2nd2")
seconde_deux[("Thevenot","Bastien")]=Student(groupe="2nd2")
seconde_deux[("Villet","Océane")]=Student(groupe="2nd2")
seconde_deux[("Virion","Valentin")]=Student(groupe="2nd2")

seconde_six={}
seconde_six[("Badets","Marine")]=Student(groupe="2nd6")
seconde_six[("Badot","Kévin")]=Student(groupe="2nd6")
seconde_six[("Bellaton","Pénélope")]=Student(groupe="2nd6")
seconde_six[("Bôle-Richard","Elodie")]=Student(groupe="2nd6")
seconde_six[("Bourgeois","Bryan")]=Student(groupe="2nd6")
seconde_six[("Brenot","Romain")]=Student(groupe="2nd6")
seconde_six[("Chapoutot","Marine")]=Student(groupe="2nd6")
seconde_six[("Chopard","Mickaël")]=Student(groupe="2nd6")
seconde_six[("Corand","Manon")]=Student(groupe="2nd6")
seconde_six[("Cousseau","Florine")]=Student(groupe="2nd6")
seconde_six[("Cretin","Rebecca")]=Student(groupe="2nd6")
seconde_six[("Cuevas","Gabrielle")]=Student(groupe="2nd6")
seconde_six[("Delhaye","Fiona")]=Student(groupe="2nd6")
seconde_six[("Di-Natale","Romain")]=Student(groupe="2nd6")
seconde_six[("Dormoy","Adrien")]=Student(groupe="2nd6")
seconde_six[("Dubief","Valentin")]=Student(groupe="2nd6")
seconde_six[("Dubrulle","Amandine")]=Student(groupe="2nd6")
seconde_six[("Fogel","Axel")]=Student(groupe="2nd6")
seconde_six[("Fontellini","Julie")]=Student(groupe="2nd6")
seconde_six[("Grenot","Emmanuel")]=Student(groupe="2nd6")
seconde_six[("Guyot","Coralie")]=Student(groupe="2nd6")
seconde_six[("Lebrasseur","Fabien")]=Student(groupe="2nd6")
seconde_six[("Leroux","Alexia")]=Student(groupe="2nd6")
seconde_six[("Mathieu","Clara")]=Student(groupe="2nd6")
seconde_six[("Moret","Manon")]=Student(groupe="2nd6")
seconde_six[("Moustakim","Ilhem")]=Student(groupe="2nd6")
seconde_six[("Paris","Joël")]=Student(groupe="2nd6")
seconde_six[("Pellegrini","Clara")]=Student(groupe="2nd6")
seconde_six[("Piguet","Louise")]=Student(groupe="2nd6")
seconde_six[("Quéré","Léa")]=Student(groupe="2nd6")
seconde_six[("Rodrigues","Maëva")]=Student(groupe="2nd6")
seconde_six[("Schindler","Sandra")]=Student(groupe="2nd6")

stmg={}
stmg[("Aucant","Anaïs")]=Student(groupe="1stmg1")
stmg[("Babet","Mauranne")]=Student(groupe="1stmg1")
stmg[("Benlarbi","Fayçal")]=Student(groupe="1stmg1")
stmg[("Bongain","Marie")]=Student(groupe="1stmg1")
stmg[("Bonnevie","Quentin")]=Student(groupe="1stmg1")
stmg[("Boujon","Agathe")]=Student(groupe="1stmg1")
stmg[("Chenut","Stéphane")]=Student(groupe="1stmg1")
stmg[("Chourfi","Marwa")]=Student(groupe="1stmg1")
stmg[("Da Mota-Païs","Ophélie")]=Student(groupe="1stmg1")
stmg[("Drissi","M'hamed")]=Student(groupe="1stmg1")
stmg[("Ekti","Melda")]=Student(groupe="1stmg1")
stmg[("Esquirol","Antoine")]=Student(groupe="1stmg1")
stmg[("Favre","Caroline")]=Student(groupe="1stmg1")
stmg[("Hachadi","Houda")]=Student(groupe="1stmg1")
stmg[("Hierholzer","Athénaïs")]=Student(groupe="1stmg1")
stmg[("Jacinto","Sarah")]=Student(groupe="1stmg1")
stmg[("Labourot","Manon")]=Student(groupe="1stmg1")
stmg[("Lesage","Kévin")]=Student(groupe="1stmg1")
stmg[("Matrat","Noémie")]=Student(groupe="1stmg1")
stmg[("Menetrier","Gautier")]=Student(groupe="1stmg1")
stmg[("Moustakim","Noëlla")]=Student(groupe="1stmg1")
stmg[("Petitjean","Marie-Lou")]=Student(groupe="1stmg1")
stmg[("Philippe","Élise")]=Student(groupe="1stmg1")
stmg[("Quenillet","Paul")]=Student(groupe="1stmg1")
stmg[("Raud","Lindsey")]=Student(groupe="1stmg1")
stmg[("Rizet","Lauraleen")]=Student(groupe="1stmg1")
stmg[("Rolet","Léo")]=Student(groupe="1stmg1")
stmg[("Rouffet","Pauline")]=Student(groupe="1stmg1")
stmg[("Soussigne","Ambre")]=Student(groupe="1stmg1")
stmg[("Verjus","Océane")]=Student(groupe="1stmg1")

tous={}
tous.update(seconde_deux)
tous.update(seconde_six)
tous.update(stmg)

for k in tous.keys():
    tous[k].nom=k[0]
    tous[k].prenom=k[1]


