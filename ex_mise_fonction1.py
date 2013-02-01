resultats=re.compile("s.").findall(texte_reference)   # Crée la liste des couples 
                                            #    «s suivit de quelque chose» 
a=random.choice(resultats)                  # Choisit un élément au hasard
                                            #   dans cette liste
return a                                    # Retourne cet élément
