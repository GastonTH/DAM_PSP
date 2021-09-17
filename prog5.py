lista = []
nValores = int(input("Cuantos valores ingresará: "))

for i in range(nValores):
    num = int(input("Dime un numero: "))
    lista.append(num) #append añade a la lista el item

print("Su lista es",lista)