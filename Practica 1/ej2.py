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

def mas_larga(lista):
    return max(lista_palabras, key=len)


#Main()
lista_palabras = ["palabra larga", "una corta", "excepcion", "hola", "esta es la mas larga de todas", "XD"]

#numero_valores = nValores

print(mas_larga(lista_palabras))