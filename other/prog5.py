def enlistar(n):
    listAux = []

    for i in range(n):
        num = int(input("Dime un numero: "))
        listAux.append(num) #append a�ade a la lista el item
    return listAux

def parImpar(listAux):

    for i in listAux:
        if i % 2 == 0:
            print("El numero es par")
        else:
            print("El numero es impar")

lista = []

while True:
    nValores = int(input("Cuantos valores ingresara: "))

    if nValores == 0:
        print("No has anyadido numeros\n")
    else:
        lista = enlistar(nValores)
        parImpar(lista)
        print("Su lista es",lista)

        break