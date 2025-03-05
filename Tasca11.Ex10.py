def dividir(a, b):
    try:
        resultat = a / b
        return resultat
    except ZeroDivisionError:
        return "Error: No es pot dividir per zero!"

#Programa principal
numerador = 10
denominador = 0
resultat = dividir(numerador, denominador)
print(resultat)
