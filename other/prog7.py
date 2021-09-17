"""n = int(input("Dime el numero de palabras: "))
listaPalabras = []

for i in range(n):
    print("-----------------")
    print("Palabra numero", i)
    palabra = str(input("Dime la palabra numero "))
    listaPalabras.append(palabra)

print("Tu lista es:", listaPalabras)
"""

def anyadir_palabras(n):
    lista = []
    for i in range(n):
        print("-----------------")
        print("Palabra numero", i + 1)
        palabra = str(input("Dime la palabra "))
        lista.append(palabra)
    return lista

numero_palabras = int(input("Dime el numero de palabras: "))
if numero_palabras == 0:
    print("No hay palabras")
else:
    listaPalabras = anyadir_palabras(numero_palabras)
    print("Tu lista es:", listaPalabras)