def Concatena_llistes(llista1, llista2, connector):
    concatenats = [a + connector + b for a, b in zip(llista1, llista2)]
    return concatenats

# Exemple d'ús:
llista1 = ['Super', 'Infra']
llista2 = ['Heroi', 'Valorat']
connector = '-'
resultat = Concatena_llistes(llista1, llista2, connector)
print(resultat)  
