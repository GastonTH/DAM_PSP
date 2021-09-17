"""Ejercicio 5
Construir un pequeño programa que convierta números binarios en enteros."""


"""
for i in range(len(str(binario))):
        print("Inicial",binario)
        to_calcule = int(binario % 10)
        
        result += to_calcule * (2**i)

        binario/=10
"""

binario = str(input("Dime un numero binario: "))
resultado = int(binario, 2)

print(resultado)
#convertir_binario(binario)