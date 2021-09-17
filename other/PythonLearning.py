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

#Main()
lista_palabras = ["palabra larga", "una corta", "excepcion", "hola", "esta es la mas larga de todas", "XD"]

print(max(lista_palabras, key=len))