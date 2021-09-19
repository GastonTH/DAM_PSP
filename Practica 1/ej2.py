"""
Ejercicio 2
Escribir una función mas_larga() que tome una lista de palabras y devuelva la más
larga."""

"""def mas_larga(lista):
    
    longitud_palabra = 0
    
    for i in lista:
        if longitud_palabra < len(i):
            longitud_palabra = len(i)

    return longitud_palabra"""

def mas_larga():

    lista = []

    numero_palabras = int(input("Cuantas palabras vas a anyadir: "))

    for i in range(numero_palabras):
        
        palabra = str(input("Dime la palabra: "))
        lista.append(palabra)

    return max(lista, key=len)

print("la palabra mas larga es:",mas_larga())