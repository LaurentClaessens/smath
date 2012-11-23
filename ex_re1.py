import re

texte="Pour qui sont ces serpents qui sifflent sur vos têtes ?"
resultats=re.compile("s.").findall(texte)
print(resultats)
