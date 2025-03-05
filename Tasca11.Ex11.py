def llegir_fitxer(prova_exercici_11):
    try:
        with open(prova_exercici_11, 'r') as fitxer:
            contingut = fitxer.read()
        return contingut
    except FileNotFoundError:
        return "Error: El fitxer no existeix."
    except IOError:
        return "Error: Hi ha hagut un problema en obrir el fitxer."

# Exemple d'ús
nom_fitxer = 'fitxer_exemple.txt'
resultat = llegir_fitxer(nom_fitxer)
print(resultat)
