"""Ejercicio 3
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y
devuelva las palabras que tengan más de n caracteres."""

def filtrar_palabras(lista, numero):

    for i in lista:
        if len(i) > numero:
            print(i)

numero_palabras = 3
lista_palabras = ["albedo", "zanahoria", "pomelo", "castillo"] 

filtrar_palabras(lista_palabras, numero_palabras)