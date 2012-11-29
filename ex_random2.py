import random

texte="Ceci est mon petit texte duquel je vais tirer des lettres au hasard."

for i in range(1,10):
    a=random.choice(texte)
    print(a)
