u=[10]  # Créer la liste contenant seulement le nombre 10

for i in range(1,100):      # Ceci ne fait que 99 étapes !
    u.append(2*u[-1])       # u[-1] est le dernier élément de la liste

print("Longueur de la liste :",len(u))   # 100
print("élément numéro 99 :",u[99])    # un grand nombre

print(u[100])   # plante
