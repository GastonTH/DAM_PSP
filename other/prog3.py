"""par = int(input("Dime un numero par "))
impar = int(input("Dime un numero impar "))

if par % 2 == 0:
    print("El par es par")
else:
    print("Es par no es par")

if impar % 2 != 0:
    print("El impar es impar")
else:
    print("Es impar no es impar")
"""

def isPar(n):
    if par % 2 == 0:
        print("El par es par")
    else:
        print("Es par no es par")

def isImpar(n):
    if impar % 2 != 0:
        print("El impar es impar")
    else:
        print("Es impar no es impar")

par = int(input("Dime un numero par "))
impar = int(input("Dime un numero impar "))

isPar(par)
isImpar(impar)