import os

# Definir el camí del directori i fitxer
directori = '/home/cicles/Ao/Prova'
fitxer = os.path.join(directori, 'Ex12.txt')

# Crear el directori
os.makedirs(directori, exist_ok=True)

# Escriure els noms dels companys de classe al fitxer
companys_de_classe = [
    "Ivan",
    "Yago",
    "Adri",
    "Ivan H.",
    "Alejandra",
    "Antonio",
    "Brais",
    "Iker",
    "JuanPablo",
    "Saad",
    "Pere",
    "Jaume",
    "David",
    "Jordi",
    "Marc",
    "Aris",
    "Lucas",
    "Eneko",
    "Pau",
    "Oscar",
    "Gustavo",
    "Bruno",
    "Alejandro"

]

with open(fitxer, 'w') as f:
    for company in companys_de_classe:
        f.write(f"{company}\n")

# Afegir els noms dels professors al fitxer
professors = [
    "David Labiano",
    "Carlos Moreno",
    "Joan Carreras",
    "Pep Malle",
    "Pepe Domínguez",
    "Clara Martín"
]

with open(fitxer, 'a') as f:
    for professor in professors:
        f.write(f"{professor}\n")

# Llegir el contingut del fitxer i posar-lo dins una llista
with open(fitxer, 'r') as f:
    llista_de_noms = f.read().splitlines()

print(llista_de_noms)
