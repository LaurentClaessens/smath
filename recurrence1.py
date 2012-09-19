u=[10]  # Créer la liste contenant seulement le nombre 10

for i in range(1,100):
    u.append(2*u[-1])       # u[-1] est le dernier élément de la liste

print(len(u))
