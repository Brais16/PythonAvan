def llista_a_diccionari(llista):
    return {valor: index for index, valor in enumerate(llista)}

# Programa Principal
llista = ["casa", "cotxe", "cadira", "taula", "Alabar", "Gabina", "Pato"]
resultat = llista_a_diccionari(llista)
print(resultat)
