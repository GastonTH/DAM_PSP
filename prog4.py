par = int(input("Dime un numero par "))

if par % 2 == 0:
    print("--> El par es par")

    impar = int(input("Dime un numero impar "))

    if impar % 2 != 0:
        print("--> El impar es impar")
    else:
        print("--> Es impar no es impar")

else:
    print("--> Es par no es par")
