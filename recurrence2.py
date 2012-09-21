# Première méthode

a=10
temps=0
while a<1000000:
    temps=temps+1
    a=a*2

print(temps)

# Seconde méthode

u=[10]
while u[-1]<1000000:
    u.append(u[-1]*2)

print(len(u))
