"""
Crear una funció que compti la longitud de cada paraula d’una cadena de caràcters que li passem. 
Utilitzar map. Ex: def lenp(frase): -- retorni una llista amb la longitud de cada paraula de la frase.
"""

def lenp(frase):
    paraules = frase.split()
    longituds = list(map(len, paraules))   
    return longituds

#Programa Principal
frase = input("Diguem quina frase vols que compti la longitud de cada paraula: ")
resultat = lenp(frase)
print(resultat)
