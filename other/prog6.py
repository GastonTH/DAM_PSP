"""numero = int(input("Dime un numero: "))
divisores = []

if numero > 0:
    print("el numero es mayor a 0")

    for i in range(numero):
        if i!=0 and numero % i == 0:
            divisores.append(i)

    print("Los divisores son", divisores)

else:
    print("el numero es menor a 0")"""

def anyadir_divisores(n):
    if n > 0:
        print("el numero es mayor a 0")

        for i in range(n+1):
            if i!=0 and n % i == 0:
                divisores.append(i)

        print("Los divisores son", divisores)

    else:
        print("el numero es menor a 0")

numero = int(input("Dime un numero: "))
divisores = []

anyadir_divisores(numero)
