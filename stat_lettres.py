import random
import re
import sys

alphabet= ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",'t','u','v',"w","x","y","z", "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S",'T','U','V',"W","X","Y","Z","é","è","à","ô","ù","î","û","œ","'",","," "] 

def texte_simple():
    return """
    L'association de deux sons peut procurer à l'oreille aussi bien une sensation d'harmonie parfaite qu'une dissonance des plus désagréables. Ce texte se propose d'expliquer les phénomènes physiques sous-jacents et d'en venir à la conclusion qu'il n'y aucun intervalle harmonieux permettant de reconstruire tous les autres.  Prérequis : pouvoir décréter qu'une association sonore est harmonieuse (ou pas) ; le nom des notes sur le piano ; le nom des intervalles ; le calcul des fractions ainsi que les puissances entières et fractionnaires ; savoir additionner des vecteurs ; quelques notions sur les unités de temps et longueur (et vitesse).  Pour différencier les octaves, on mettra un nombre en exposant. Par exemple, le troisième (du piano) en partant des graves, de même désignera le cinquième si bémol.  Deux expériences Harmoniques d'une note d'un piano Frapper le  sur un piano et écouter en mettant la pédale : d'autres notes se font entendre, d'autant plus faiblement qu'elles sont aigües. Dans l'ordre, on liste Pour entendre les notes les plus aigües, on pourra enfoncer la touche correspondante sans produire la note, puis lever la pédale : il devrait rester un résidu sonore de hauteur souhaitée.  Ces notes supplémentaires sont appelées harmoniques de la première note que l'on a fait sonner (ici le do), laquelle est aussi appelée harmonique fondamentale.  Si l'on fait la même expérience avec une autre note, par exemple en prenant pour fondamentale un mi, on entendra les harmoniques suivantes Le musicien observera que les intervalles successifs sont les mêmes : octave quinte, quarte, tierce majeure, tierce mineure deux fois, seconde majeure, seconde majeure trois fois, seconde mineure...  et que la complexité des intervalles va également croissant : on va de l'octave à la seconde mineure en passant par la quinte puis les tierces. 
    Qu'est-ce qui se cache derrière ces suites ?  Le réchauffement observé pendant plusieurs décennies a été relié aux changements survenus dans le cycle hydrologique à grande échelle, notamment: l'augmentation de la teneur en vapeur d'eau de l'atmosphère, la modification de la configuration, de l'intensité et des extrêmes des précipitations, la diminution de la couverture neigeuse et la fonte des glaces accrue, ainsi que la modification de l'humidité du sol et du ruissellement. Les changements dans les précipitations sont très variables à l'échelle spatiale et d'une décennie à l'autre. Au cours du XXe siècle, les précipitations ont surtout augmenté sur les continents dans les latitudes les plus septentrionales, tandis que des diminutions ont principalement touché les latitudes comprises entre 10°S et 30°N depuis les années 1970. La fréquence des épisodes de fortes précipitations (ou la partie des précipitations totales imputable à de fortes pluies) a augmenté dans la plupart des régions (probable). Au niveau mondial, la superficie des terres considérées comme très sèches a plus que doublé depuis les années 1970 (probable). Le volume d'eau stocké dans les glaciers de montagne et la couverture neigeuse de l'hémisphère Nord a considérablement diminué. On a observé des décalages dans les variations saisonnières du débit des rivières alimentées par la fonte des glaciers et de la neige et dans les phénomènes liés à la glace dans les rivières et les lacs (degré de confiance élevé).  On ne dispose que de très peu de mesures directes de l'évapotranspiration effective sur l'ensemble des terres émergées du globe, alors que les produits d'analyse mondiaux sont sensibles aux types d'analyses effectuées et peuvent renfermer d'importantes erreurs, rendant impossible leur utilisation pour l'analyse des tendances. Par conséquent, il n'existe que peu de littérature sur les tendances observées en matière d'évapotranspiration réelle ou potentielle. Évaporation mesurée au bac.
    """

def fichier_texte(nom):
    print("Lecture du fichier")
    f=open(nom)
    texte_original=f.read()
    return texte_original

texte_original=texte_simple()
#texte_original=fichier_texte("temps_perdu.txt")
texte_original=fichier_texte("Sherlock.txt")

print("Création du texte final")
texte_final=texte_original.replace("(","").replace(")","").replace(";","").replace("  ","").replace("\n"," ").replace("-","").replace(":","").replace("?","").replace("   "," ")
while "  " in texte_final:
    texte_final=texte_final.replace("  "," ")

def texte_to_position(texte_final):

    position={}
    for l in alphabet:
        position[l]=[i for i in range(0,len(texte_final)) if texte_final[i]==l]
    return position

position=texte_to_position(texte_final)

def suivante_markov(x):
    if x == ".":
        return " "
    i=random.choice(position[x])
    if texte_final[i] != x:
        print("hum")
    k=1
    while texte_final[i+k] not in alphabet:
        k=k+1
    return texte_final[i+k]

dico_double={}

if int(sys.argv[1])==0:
    liste_lettres=[x for x in list(texte_final) if x in alphabet]

def suivante_double(texte,n=2):
    if n==0:
        a=""
        while a not in alphabet:
            a = random.choice(texte_final)
        return a

    a_trouver=texte[-n:]    # les n dernières lettres de  `texte`
    # À ce niveau, il peut y avoir deux problèmes.
    # - Il pourrait n'avoir aucun `a_trouver` dans le texte
    # - Il pourrait y en avoir deux d'affilée.
    A=texte_final.split(a_trouver)[1:]  # Le premier ne compte pas.
    if len(A)==1:       # C'est le cas où le truc n'existe pas
        return suivante_double(texte,n-1)
    l=random.choice(A)
    try :
        return l[0]
    except IndexError :
        # Dans ce cas, c'est que la liste est vide, c'est à dire que `a_trouver` apparaît deux fois d'affilée.
        # Donc on retourne la première lettre de `a_trouver`
        return a_trouver[0]

n=2
if sys.argv:
    n=int(sys.argv[1])
nouveau=""
for i in range(0,n):
    nouveau=nouveau+random.choice(alphabet)

for i in range(1,500):
    nouveau=nouveau+suivante_double(nouveau,n)

print("".join(nouveau))
