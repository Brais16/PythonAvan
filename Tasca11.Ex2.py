from functools import reduce

def Passar_a_Numero(llista):
    numero = reduce(lambda x, y: x * 10 + y, llista)
    return numero

# Programa Principal
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
resultat = Passar_a_Numero(digits)
print(resultat)
