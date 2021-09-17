"""n = int(input("Dime el numero de palabras: "))
listaPalabras = []
contador = 0;

for i in range(n):
    print("-----------------")
    print("Palabra numero", i + 1)
    palabra = str(input("Dime la palabra numero "))
    listaPalabras.append(palabra)

buscada = str(input("\nQue palabra quieres buscar: "))

for i in range(len(listaPalabras)):
    if listaPalabras[i] == buscada:
        contador+=1
print("Tu palabra buscada es:", buscada, "y hay", contador, "coincidencias en tu lista\n ----", listaPalabras)
"""
def anyadir_palabras(n):
    lista = []
    for i in range(n):
        print("-----------------")
        print("Palabra numero", i + 1)
        palabra = str(input("Dime la palabra numero "))
        lista.append(palabra)
    return lista
def buscador(palabra, lista):

    contador = 0

    for i in range(len(lista)):
        if lista[i] == palabra:
            contador+=1

    print("Tu palabra buscada es:", palabra, "y hay", contador, "coincidencias en tu lista\n ----", lista)

numero_palabras = int(input("Dime el numero de palabras: "))

if numero_palabras == 0:
    print("No hay palabras")
else:

    listaPalabras = anyadir_palabras(numero_palabras)
    buscada = str(input("\nQue palabra quieres buscar: "))
    buscador(buscada, listaPalabras)