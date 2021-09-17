
def media(lista):
    res = (lista[0] + lista[1]) / 2
    return round(res, 3)


numero1 = int(input("numero 1 = "))
numero2 = int(input("numero 2 = "))

print("los numero son:", numero1, "y", numero2)

lista = [numero1, numero2]

print("y la lista", lista)

print("la media da", media(lista))

