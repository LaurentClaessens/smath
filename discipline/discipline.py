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

for et in tous.values():
    print(et.prenom,et.nom)


tous[("Atzorivenne","Mathis")].append_bar(1,10,9999,"DM pas fait : melons et pommes")
tous[("Atzorivenne","Mathis")].append_bar(12,10,2012,"Lance un objet")

#Bailly, Thomas
#Bauche, Léa

tous[("Besancon","Séphora")].append_bar(1,10,9999,"DM pas fait : melons et pommes")


tous[("Besnier","Romain")].append_bar(1,1,9999,"DM pas fait : melons et pommes")
tous[("Besnier","Romain")].append_bar(28,9,2012,"Lancer un objet")
tous[("Besnier","Romain")].append_bar(8,10,2012,"est debout")
tous[("Besnier","Romain")].append_bar(15,10,2012,"est debout")
tous[("Besnier","Romain")].append_bar(15,10,2012,"siffle")
tous[("Besnier","Romain")].append_bar(22,10,2012,"bavardage")
tous[("Besnier","Romain")].append_colle(16,10,2012,motif=None)


tous[("Blanchot","Noé")].append_colle(11,10,1000,"bavardage incessant depuis le début du mois d'octobre, y compris pendan la séance en salle informatique (1 octobre, 4 octobre, 8 octobre et 8 octobre en salle info.)")

tous[("Blanchot","Noé")].append_bar(11,10,2012,"bavardage")
tous[("Blanchot","Noé")].append_bar(12,10,2012,"bavardage")
tous[("Blanchot","Noé")].append_bar(15,10,2012,"bavardage")
tous[("Blanchot","Noé")].append_bar(19,10,2012,"bavardage durant l'intérogation")
tous[("Blanchot","Noé")].append_bar(22,10,2012,"bavardage")

print([x.motif for x in tous[("Blanchot","Noé")].croix])



tous[("Caretti","Arno")].append_bar(1,10,2012,"debout")
tous[("Caretti","Arno")].append_bar(1,10,9999,"DM pas fait : melons et pommes")


tous[("Colin","Mathieu")].append_bar(15,10,2012,"Lance un objet")
tous[("Colin","Mathieu")].append_bar(15,10,2012,"bruitages et bavardages incessants")
tous[("Colin","Mathieu")].append_bar(19,10,2012,"cahier fermé")
tous[("Colin","Mathieu")].append_bar(22,10,2012,"bavardage")

tous[("Dole","Cynthia")].append_bar(15,10,2012,"parle avec Noé durant tout le cours en groupe")


#Dominot, Charline
#Giroux, Adeline

tous[("Gras","Guillaume")].append_bar(1,10,2012,"bavardage")
tous[("Gras","Guillaume")].append_bar(1,10,2012,"debout")
tous[("Gras","Guillaume")].append_bar(15,10,2012,"bavardage")
tous[("Gras","Guillaume")].append_bar(22,10,2012,"bavardage")

#Guenard, Florian

tous[("Guillot","Anthony")].append_bar(1,10,2012,"debout")
tous[("Guillot","Anthony")].append_bar(11,10,2012,"bavardage")
tous[("Guillot","Anthony")].append_bar(12,10,2012,"cahier fermé")

tous[("Koehler","Paul-Erwan")].append_bar(1,10,9999,"DM pas fait : histogrammes")
tous[("Koehler","Paul-Erwan")].append_bar(1,10,9999,"DM pas fait : melons et pommes")
tous[("Koehler","Paul-Erwan")].append_bar(11,10,2012,"bavardage")
tous[("Koehler","Paul-Erwan")].append_bar(12,10,2012,"se chamaille en continu avec Raphaël")


tous[("Kuti","Belinda")].append_bar(1,10,9999,"DM pas fait : histogrammes")
tous[("Kuti","Belinda")].append_bar(12,10,2012,"cahier fermé")
tous[("Kuti","Belinda")].append_bar(22,10,2012,"parle trop et fait la chèvre")


#Larderet, Etienne

tous[("Letondor-Lavrut","Claire")].append_bar(4,10,2012,"lance un objet")
tous[("Letondor-Lavrut","Claire")].append_bar(22,10,2012,"parle trop")


tous[("Limoge","Thibaut")].append_bar(11,10,2012,"bavardage")
tous[("Limoge","Thibaut")].append_bar(22,10,2012,"bavardage")

#Mougeot, Romain

tous[("Navel","Rémi")].append_bar(4,10,2012,"bavardage")
tous[("Navel","Rémi")].append_bar(8,10,2012,"crée des répertoires aux noms idiots en salle info")
tous[("Navel","Rémi")].append_bar(11,10,2012,"bavardage")
tous[("Navel","Rémi")].append_bar(12,10,2012,"bavardage")


tous[("Pardon","Mélanie")].append_bar(1,1,9999,"DM pas fait : melons et pommes")
tous[("Pardon","Mélanie")].append_bar(11,10,2012,"bavardage")


#Perrault, Mélanie

tous[("Pillot","César")].append_bar(1,10,2012,"bavardage")
tous[("Pillot","César")].append_bar(1,1,9999,"DM pas fait : histogrammes")

tous[("Préaud","Raphaël")].append_bar(1,10,2012,"bavardage")
tous[("Préaud","Raphaël")].append_bar(4,10,2012,"frappe César avec un stylo")
tous[("Préaud","Raphaël")].append_bar(12,10,2012,"se chamaille en continu avec Paul-Erwan")
tous[("Préaud","Raphaël")].append_bar(22,10,2012,"bavardage en groupe et en classe complète")

tous[("Robert","Jérémy")].append_bar(1,10,2012,"bavardage")
tous[("Robert","Jérémy")].append_bar(12,10,2012,"insulte Raphaël")
tous[("Robert","Jérémy")].append_bar(12,10,2012,"cahier fermé")
tous[("Robert","Jérémy")].append_bar(15,10,2012,"insulte Raphaël")
tous[("Robert","Jérémy")].append_bar(15,10,2012,"tente de coller du papier collant sur Laura")
tous[("Robert","Jérémy")].append_bar(15,10,2012,"cahier fermé")

tous[("Robert","Jérémy")].append_colle(16,10,2012)

tous[("Robert","Jérémy")].append_colle(22,10,2012,extra=True,motif=""" Jette sa trousse par la fenêtre et sort de la classe de son propre chef pour aller la chercher, malgré une interdiction totalement explicite du professeur. Son excuse : «j'ai pas fait exprès : je visais Rémi».""")

tous[("Robert","Jérémy")].append_bar(22,10,2012,"bavardage")



tous[("Tepinier","Laura")].append_bar(4,10,2012,"bavardage")
tous[("Tepinier","Laura")].append_bar(11,10,2012,"bavardage")
tous[("Tepinier","Laura")].append_bar(12,10,2012,"cahier fermé")
tous[("Tepinier","Laura")].append_bar(22,10,2012,"bavardage")
tous[("Tepinier","Laura")].append_bar(22,10,2012,"cahier fermé")

tous[("Thevenot","Bastien")].append_bar(22,10,2012,"bavardage")

tous[("Villet","Océane")].append_bar(12,10,2012,"cahier fermé")
tous[("Villet","Océane")].append_bar(15,10,2012,"cahier fermé")
tous[("Villet","Océane")].append_bar(19,10,2012,"lance une bouteille d'eau")


tous[("Virion","Valentin")].append_bar(11,10,2012,"bavardage")

#tous[("Badets","Marine")].append_bar(<++>,<++>,2012,"<++>")
#tous[("Badot","Kévin")].append_bar(<++>,<++>,2012,"<++>")
#tous[("Bellaton","Pénélope")].append_bar(<++>,<++>,2012,"<++>")

tous[("Bôle-Richard","Elodie")].append_bar(8,10,2012,"bavardage")
tous[("Bôle-Richard","Elodie")].append_bar(16,10,2012,"bavardage")

tous[("Bourgeois","Bryan")].append_bar(22,10,2012,"bavardage")

#tous[("Brenot","Romain")].append_bar(<++>,<++>,2012,"<++>")
#tous[("Chapoutot","Marine")].append_bar(<++>,<++>,2012,"<++>")

tous[("Chopard","Mickaël")].append_bar(16,10,2012,"bavardage en continu avec Gabrielle et Rebecca")
tous[("Chopard","Mickaël")].append_bar(16,10,2012,"pré-colle")
tous[("Chopard","Mickaël")].append_bar(22,10,2012,"bavardage en continu avec les mêmes")

#tous[("Corand","Manon")].append_bar(<++>,<++>,2012,"<++>")
#tous[("Cousseau","Florine")].append_bar(<++>,<++>,2012,"<++>")

tous[("Cretin","Rebecca")].append_bar(16,10,2012,"bavardage en continu avec Mickaël et Gabrielle")
tous[("Cretin","Rebecca")].append_bar(16,10,2012,"pré-colle")
tous[("Cretin","Rebecca")].append_bar(22,10,2012,"bavardage")

tous[("Cuevas","Gabrielle")].append_bar(16,10,2012,"bavardage en continu avec Mickaël et Rebecca")
tous[("Cuevas","Gabrielle")].append_bar(22,10,2012,"bavardage en continu avec les mêmes")

#tous[("Delhaye","Fiona")].append_bar(<++>,<++>,2012,"<++>")

tous[("Di-Natale","Romain")].append_bar(16,10,2012,"pré-colle")
tous[("Di-Natale","Romain")].append_bar(22,10,2012,"bavardage")



tous[("Dormoy","Adrien")].append_bar(16,10,2012,"bavardage")
tous[("Dormoy","Adrien")].append_bar(16,10,2012,"pré-colle")
tous[("Dormoy","Adrien")].append_bar(16,10,2012,"cahier fermé")
tous[("Dormoy","Adrien")].append_bar(22,10,2012,"bavardage")

#tous[("Dubief","Valentin")].append_bar(<++>,<++>,2012,"<++>")
#tous[("Dubrulle","Amandine")].append_bar(<++>,<++>,2012,"<++>")
#tous[("Fogel","Axel")].append_bar(<++>,<++>,2012,"<++>")
#tous[("Fontellini","Julie")].append_bar(<++>,<++>,2012,"<++>")
#tous[("Grenot","Emmanuel")].append_bar(<++>,<++>,2012,"<++>")

tous[("Guyot","Coralie")].append_bar(11,10,2012,"cherche des images d'Apu sur internet pendant le scéance info")


#tous[("Lebrasseur","Fabien")].append_bar(<++>,<++>,2012,"<++>")
#tous[("Leroux","Alexia")].append_bar(<++>,<++>,2012,"<++>")
#tous[("Mathieu","Clara")].append_bar(<++>,<++>,2012,"<++>")
#tous[("Moret","Manon")].append_bar(<++>,<++>,2012,"<++>")

tous[("Moustakim","Ilhem")].append_bar(8,10,2012,"bavardage")
tous[("Moustakim","Ilhem")].append_bar(11,10,2012,"cherche des images d'Apu sur internet en salle info")
tous[("Moustakim","Ilhem")].append_bar(16,10,2012,"bavardage")
tous[("Moustakim","Ilhem")].append_bar(22,10,2012,"bavardage")


#tous[("Paris","Joël")].append_bar(<++>,<++>,2012,"<++>")

tous[("Pellegrini","Clara")].append_bar(16,10,2012,"bavardage")
tous[("Pellegrini","Clara")].append_bar(22,10,2012,"bavardage")

#tous[("Piguet","Louise")].append_bar(<++>,<++>,2012,"<++>")

tous[("Quéré","Léa")].append_bar(16,10,2012,"bavardage")
tous[("Quéré","Léa")].append_bar(16,10,2012,"répète «Le premier qui moufte» pour se moquer du prof.")
#pré-colle le 16 octobre (répète «le premier qui moufte ...» pour se moquer du prof)



tous[("Rodrigues","Maëva")].append_bar(16,10,2012,"bavardage")



#tous[("Schindler","Sandra")].append_bar(<++>,<++>,2012,"<++>")


Les pré-colles
Athénaïs
Jacinto, Sarah
Ambre



tous[("Aucant","Anaïs")].append_bar(15,10,2012,"bavardage")


tous[("Babet","Mauranne")].append_bar(15,10,2012,"bavardage")


#tous[("Benlarbi","Fayçal")].append_bar(<++>,<++>,2012,"<++>")


tous[("Bongain","Marie")].append_bar(15,10,2012,"bavardage")

tous[("Bonnevie","Quentin")].append_bar(8,10,2012,"bavardage")

tous[("Boujon","Agathe")].append_bar(15,10,2012,"bavardage")
tous[("Boujon","Agathe")].append_bar(19,10,2012,"bavardage")


#tous[("Chenut","Stéphane")].append_bar(<++>,<++>,2012,"<++>")

tous[("Chourfi","Marwa")].append_bar(2,10,2012,"cahier fermé")
tous[("Chourfi","Marwa")].append_bar(19,10,2012,"bavardage")

#tous[("Da Mota-Païs","Ophélie")].append_bar(<++>,<++>,2012,"<++>")

tous[("Drissi","M'hamed")].append_bar(8,10,2012,"joue avec un briquet")
tous[("Drissi","M'hamed")].append_bar(8,10,2012,"bavardage")
tous[("Drissi","M'hamed")].append_bar(16,10,2012,"bavardage")


#tous[("Ekti","Melda")].append_bar(<++>,<++>,2012,"<++>")

tous[("Esquirol","Antoine")].append_bar(15,10,2012,"bavardage")
tous[("Esquirol","Antoine")].append_bar(16,10,2012,"bavardage")
tous[("Esquirol","Antoine")].append_colle(8,10,2012,motif="A un téléphone en main durant le cours du 8 octobre.\n Note a posteriori : n'assume pas ses responsabilités : a laissé Agathe se dénoncer à sa place.",extra=True)

#Favre, Caroline
#Hachadi, Houda   # Note pour quelque part : elle n'a pas rendu le DS : je l'ai entendu dire.

tous[("Hierholzer","Athénaïs")].append_bar(1,10,2012,"lancer")
tous[("Hierholzer","Athénaïs")].append_bar(8,10,2012,"bavardage")
tous[("Hierholzer","Athénaïs")].append_bar(15,10,2012,"bavardage")
tous[("Hierholzer","Athénaïs")].append_bar(19,10,2012,"pré-colle")

#Jacinto, Sarah
tous[("Labourot","Manon")].append_bar(16,10,2012,"pré-colle")

==================================================


A déjà pris une retenue pour motif :


tous[("Lesage","Kévin")].append_bar(1,10,2012,"cahier fermé")
tous[("Lesage","Kévin")].append_bar(2,10,2012,"est debout")
tous[("Lesage","Kévin")].append_bar(2,10,2012,"bavardage")
tous[("Lesage","Kévin")].append_colle(2,10,2012)
#Cette colle a été faite le 17 octobre et les exercices ont été fait de façon complètement fausses.

tous[("Lesage","Kévin")].append_bar(8,10,2012,"bavardage")
tous[("Lesage","Kévin")].append_bar(15,10,2012,"bavardage")


tous[("Matrat","Noémie")].append_bar(16,10,2012,"bavardage")

tous[("Menetrier","Gautier")].append_bar(2,10,2012,"est encore debout")
tous[("Menetrier","Gautier")].append_bar(16,10,2012,"est debout")


==================================================
tous[("Moustakim","Noëlla")].append_bar(<++>,<++>,2012,"<++>")
Bavardage le 19 octobre
==================================================

Petitjean, Marie-Lou
Philippe, Élise
Quenillet, Paul
tous[("Raud","Lindsey")].append_bar(<++>,<++>,2012,"<++>")
"
bavardage 15 octobre


==============================================
tous[("Rizet","Lauraleen")].append_bar(<++>,<++>,2012,"<++>")
bavardage le 16 octobre

A déjà une colle pour motif :
A un téléphone en main durant le cours du 2 octobre. Préfère avoir une colle que de voir le téléphone confisqué chez le CPE.

==============================================
Rolet, Léo
Rouffet, Pauline

==============================================
tous[("Soussigne","Ambre")].append_bar(<++>,<++>,2012,"<++>")
bavardage le 2 octobre
debout le 2 octobre
cahier fermé le 12 octobre
pré-colle le 16 octobre
==============================================


Verjus, Océane



"""
