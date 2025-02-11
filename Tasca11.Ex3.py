def Paraules_per_Lletra(llista, lletra):
    paraules_filtrades = list(filter(lambda paraula: paraula.startswith(lletra), llista))
    return paraules_filtrades

# Programa Principal
paraules = ["Jairo", "Tomatic", "Alexander", "Elias", "España"]
lletra = "E"
resultat = Paraules_per_Lletra(paraules, lletra)
print(resultat) 
