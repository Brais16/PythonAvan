def valors_i_indexos_iguals(llista):
    return sum(1 for index, valor in enumerate(llista) if index == valor)

# Programa Principal
llista = [0, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
resultat = valors_i_indexos_iguals(llista)
print(resultat)  
